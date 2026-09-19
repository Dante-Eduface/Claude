#!/usr/bin/env python3
"""Grendel op alles wat een prospect bereikt of credits kost.

Twee niveaus, en het onderste is er sinds 16-09-2026 omdat de bescherming die
er hoorde te zijn stilletjes was weggevallen:

1. ALTIJD, in elke sessie: verstuur-, import- en credit-tools vragen eerst om
   toestemming. Dat stond in settings.json als `ask`-regels op namen als
   `mcp__lemlist__send_message`, maar de connector heet in de praktijk
   `mcp__<uuid>__send_message`. Geen enkele regel matchte nog, dus het besluit
   van 09-06-2026 dat er nooit automatisch iets verstuurd wordt, rustte maanden
   op niets. Deze hook matcht op de TOOLNAAM aan het eind, dus hij blijft werken
   als de connector-id verandert.

2. TIJDENS DE NACHTRONDE (SHIFT_NACHT=1): dezelfde tools worden geweigerd in
   plaats van bevraagd. Die ronde draait met --permission-mode bypassPermissions,
   want er is niemand om een vraag te beantwoorden, en daarmee vervalt elke
   ask-regel. Een instructie in een prompt is een verzoek, dit is een grendel.

Ontwerpkeuze: matchen op de staart van de toolnaam, niet op de server. Een
regel die de server noemt gaat kapot zodra een connector opnieuw gekoppeld
wordt, en dat is precies wat hier is misgegaan.
"""
import json
import os
import re
import sys

# Alles wat een prospect bereikt, geld kost, of een campagne in beweging zet.
NAAR_BUITEN = re.compile(
    r"(^|__)(send_message|send_task|launch_campaign|set_campaign_state"
    r"|add_leads_to_campaign|import_leads_to_campaign|push_leads_to_contacts"
    r"|add_contacts_to_list|copy_campaign_leads"
    r"|enrich_lead|bulk_enrich_leads|bulk_enrich_data|enrich_field"
    r"|create_draft_email|update_draft_email"
    r"|purchase_domain|provision_mailboxes"
    r"|add_sequence_step|update_sequence_step|delete_sequence_step)$"
)
# Verwijderen is in een onbewaakte ronde nooit nodig, en ook overdag het
# soort actie waar je even naar wilt kijken.
VERWIJDEREN = re.compile(r"(^|__)delete_[a-z_]+$")


def beslis(tool):
    """(beslissing, reden) of None als deze tool ons niet aangaat."""
    nacht = os.environ.get("SHIFT_NACHT") == "1"
    if NAAR_BUITEN.search(tool):
        wat = ("stuurt iets naar buiten of kost credits" if "enrich" not in tool
               else "kost credits")
        if nacht:
            return "deny", ("%s %s. De nachtronde schrijft alleen concepten; Dante keurt ze "
                            "'s ochtends goed en zet ze zelf in Lemlist." % (tool, wat))
        return "ask", "%s %s. Even bevestigen voor het echt gebeurt." % (tool, wat)
    if VERWIJDEREN.search(tool):
        if nacht:
            return "deny", "%s verwijdert gegevens. Dat doet een onbewaakte ronde niet." % tool
        return "ask", "%s verwijdert gegevens." % tool
    return None


def main():
    try:
        invoer = json.load(sys.stdin)
    except Exception:
        sys.exit(0)                  # onleesbare invoer is geen reden om werk te blokkeren

    uitslag = beslis(invoer.get("tool_name", ""))
    if uitslag:
        beslissing, reden = uitslag
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": beslissing,
                "permissionDecisionReason": reden,
            }
        }))
    sys.exit(0)


if __name__ == "__main__":
    main()
