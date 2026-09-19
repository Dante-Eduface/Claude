#!/usr/bin/env python3
"""
transcribe.py - audio naar tekst met faster-whisper, lokaal en zonder ffmpeg.

Werkt op elk audio- of videobestand dat PyAV kan lezen: mp3, m4a, wav, aac,
flac, ogg, opus, mp4, mov, webm. Er is GEEN ffmpeg-binary nodig, faster-whisper
decodeert zelf via PyAV.

    python3 .claude/scripts/transcribe.py opname.mp3
    python3 .claude/scripts/transcribe.py call.mp3 --kwaliteit goed --taal nl
    python3 .claude/scripts/transcribe.py lange-call.m4a --kwaliteit beste --srt

Standaard schrijft hij <bestandsnaam>.txt naast het audiobestand en print hij
de tekst ook naar stdout. Met --srt komt er ook een .srt met tijdstempels bij.

TWEE STANDEN (--kwaliteit):
  snel = small           korte fragmenten en memo's, ongeveer 2.9x realtime
  goed = large-v3-turbo  gesprekken en lange calls, ongeveer 2.0x realtime

Turbo is op deze machine gemeten zowel sneller als beter dan medium, dus er is
geen reden om medium te kiezen. Medium staat wel gecached: --model medium.
"beste" is een alias voor "goed". Met --model kun je elk faster-whisper-model
kiezen; alles buiten small, medium en large-v3-turbo wordt eerst gedownload.

LANGE BESTANDEN (een uur of meer):
Echt gemeten op deze Mac (Intel i5, 4 cores, 16 GB) op een bestand van 2h02m:
35m40s met --kwaliteit snel, oftewel 3.4x realtime. Met --kwaliteit goed duurt
datzelfde bestand ongeveer een uur.

Let op het geheugen: faster-whisper decodeert het HELE bestand in RAM voordat
het begint. Bij 2 uur audio piekte het proces op 5,8 GB. Dat past in 16 GB,
maar sluit zware programma's af bij bestanden van 3 uur of langer, of knip het
bestand dan eerst in stukken.
De tekst wordt tijdens het transcriberen weggeschreven, regel voor regel. Breekt
het af, dan staat alles tot dat moment al in het .txt-bestand. Ondertussen komt
er elke 30 seconden een voortgangsregel met percentage en verwachte resttijd.
Draai lange klussen in de achtergrond en kijk in het logbestand:

    python3 .claude/scripts/transcribe.py call.mp3 --kwaliteit beste --stil > log.txt 2>&1 &
"""

import argparse
import os
import sys
import time

AUDIO_EXT = {
    ".mp3", ".m4a", ".wav", ".aac", ".flac", ".ogg", ".oga", ".opus",
    ".wma", ".aiff", ".aif", ".mp4", ".mov", ".m4v", ".webm", ".mkv", ".avi",
}

KWALITEIT = {
    "snel": "small",
    "goed": "large-v3-turbo",
    "beste": "large-v3-turbo",
}

VOORTGANG_ELKE = 30  # seconden tussen twee voortgangsregels


def tijdstempel(seconden):
    """srt-formaat: 00:01:02,500"""
    ms = int(round(seconden * 1000))
    u, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{u:02d}:{m:02d}:{s:02d},{ms:03d}"


def klok(seconden):
    """1h04m of 3m12s, voor voortgang en resttijd."""
    seconden = int(max(0, seconden))
    u, rest = divmod(seconden, 3600)
    m, s = divmod(rest, 60)
    if u:
        return f"{u}h{m:02d}m"
    if m:
        return f"{m}m{s:02d}s"
    return f"{s}s"


def controleer_bestand(pad):
    """Geeft een foutmelding terug, of None als het bestand bruikbaar lijkt."""
    if not os.path.exists(pad):
        return "bestaat niet"
    if os.path.isdir(pad):
        return "is een map"
    if os.path.getsize(pad) == 0:
        return "is leeg (0 bytes)"
    ext = os.path.splitext(pad)[1].lower()
    if ext and ext not in AUDIO_EXT:
        return f"extensie {ext} is geen audio/video, sla over"
    return None


def laad_model(naam, compute_type, threads):
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        sys.exit(
            "faster-whisper ontbreekt. Installeer met:\n"
            "    python3 -m pip install --user faster-whisper\n"
            "PyAV en ctranslate2 komen automatisch mee, ffmpeg is niet nodig."
        )
    try:
        return WhisperModel(
            naam, device="cpu", compute_type=compute_type, cpu_threads=threads
        )
    except Exception as fout:
        sys.exit(
            f"model '{naam}' kon niet geladen worden: {fout}\n"
            "Zonder internet werkt alleen een model dat al in "
            "~/.cache/huggingface/hub staat (small, medium, large-v3-turbo)."
        )


def transcribeer(model, pad, args):
    reden = controleer_bestand(pad)
    if reden:
        print(f"[overgeslagen] {pad}: {reden}", file=sys.stderr)
        return False

    try:
        segmenten, info = model.transcribe(
            pad,
            language=args.taal,
            beam_size=args.beam,
            vad_filter=not args.geen_vad,
            condition_on_previous_text=False,
        )
    except Exception as fout:
        print(f"[mislukt] {pad}: {fout}", file=sys.stderr)
        return False

    basis = os.path.splitext(os.path.basename(pad))[0]
    map_uit = args.uit or os.path.dirname(os.path.abspath(pad))
    os.makedirs(map_uit, exist_ok=True)
    pad_txt = os.path.join(map_uit, basis + ".txt")
    pad_srt = os.path.join(map_uit, basis + ".srt") if args.srt else None

    duur = getattr(info, "duration", 0) or 0
    print(
        f"[start] {pad} ({klok(duur)} audio, taal {info.language}, model {args.model})",
        file=sys.stderr,
    )

    begin = time.time()
    laatste_melding = begin
    aantal = 0
    fout_tijdens = None

    # Regel voor regel wegschrijven: bij een crash of ctrl-c staat alles tot
    # dat moment al op schijf. Daarom geen list() over de segmenten.
    f_txt = open(pad_txt, "w", encoding="utf-8")
    f_srt = open(pad_srt, "w", encoding="utf-8") if pad_srt else None
    try:
        for segment in segmenten:
            tekst = segment.text.strip()
            aantal += 1
            if tekst:
                f_txt.write(tekst + "\n")
                f_txt.flush()
                if not args.stil:
                    print(tekst, flush=True)
            if f_srt:
                f_srt.write(f"{aantal}\n")
                f_srt.write(f"{tijdstempel(segment.start)} --> {tijdstempel(segment.end)}\n")
                f_srt.write(tekst + "\n\n")
                f_srt.flush()

            nu = time.time()
            if duur and nu - laatste_melding >= VOORTGANG_ELKE:
                laatste_melding = nu
                verstreken = nu - begin
                deel = min(segment.end / duur, 0.999)
                rest = verstreken / deel - verstreken if deel > 0 else 0
                print(
                    f"[bezig] {basis}: {deel * 100:.0f}% "
                    f"({klok(segment.end)} van {klok(duur)}), "
                    f"nog ongeveer {klok(rest)}",
                    file=sys.stderr,
                    flush=True,
                )
    except KeyboardInterrupt:
        fout_tijdens = "afgebroken met ctrl-c"
    except Exception as fout:
        fout_tijdens = str(fout)
    finally:
        f_txt.close()
        if f_srt:
            f_srt.close()

    verstreken = time.time() - begin
    snelheid = f", {duur / verstreken:.1f}x realtime" if duur and verstreken else ""
    if fout_tijdens:
        print(
            f"[deels] {pad}: {fout_tijdens}. Wat af was staat in {pad_txt}",
            file=sys.stderr,
        )
        return False
    print(
        f"[klaar] {pad} in {klok(verstreken)}{snelheid} -> {pad_txt}",
        file=sys.stderr,
    )
    return True


def main():
    p = argparse.ArgumentParser(description="Audio naar tekst met faster-whisper.")
    p.add_argument("bestanden", nargs="+", help="audio- of videobestanden")
    p.add_argument("--kwaliteit", choices=list(KWALITEIT), default="snel",
                   help="snel (small) of goed (large-v3-turbo); beste = alias voor goed")
    p.add_argument("--model", default=None,
                   help="overschrijft --kwaliteit; elk faster-whisper-model")
    p.add_argument("--taal", default=None,
                   help="nl of en; leeg laten = automatisch herkennen")
    p.add_argument("--uit", default=None, help="map voor de output (standaard naast het bestand)")
    p.add_argument("--srt", action="store_true", help="ook een .srt met tijdstempels")
    p.add_argument("--beam", type=int, default=5, help="beam size, hoger = preciezer en trager")
    p.add_argument("--compute", default="int8", help="int8 (standaard), int8_float32, float32")
    p.add_argument("--threads", type=int, default=0, help="cpu-threads, 0 = zelf bepalen")
    p.add_argument("--geen-vad", action="store_true",
                   help="stiltefilter uit; gebruik dit als er tekst wegvalt")
    p.add_argument("--stil", action="store_true",
                   help="niet naar stdout printen, alleen wegschrijven en voortgang tonen")
    args = p.parse_args()

    if not args.model:
        args.model = KWALITEIT[args.kwaliteit]

    model = laad_model(args.model, args.compute, args.threads)

    gelukt = 0
    for pad in args.bestanden:
        if transcribeer(model, pad, args):
            gelukt += 1

    mislukt = len(args.bestanden) - gelukt
    if mislukt:
        print(f"\n{gelukt} gelukt, {mislukt} mislukt.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
