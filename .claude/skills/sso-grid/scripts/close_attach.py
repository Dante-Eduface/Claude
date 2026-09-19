#!/usr/bin/env python3
"""Hang een SSO-grid PNG als bijlage onder een nieuwe note op een Close-lead.

De Close MCP-server kan geen bijlagen aanmaken, dus dit gaat via de REST API:
  1. POST /files/upload/   -> signed S3 POST + download-url
  2. POST naar S3          -> het bestand er echt heen (binnen 60s)
  3. POST /activity/note/  -> note met attachments[]

Gebruik:
  CLOSE_API_KEY=api_xxx python3 close_attach.py \
      --lead-id lead_xxx --png pad/naar/grid.png --title "SSO grid 1"

De S3-url is 24 uur geldig; Close kopieert het bestand bij het aanmaken van de note.
"""
import argparse
import mimetypes
import os
import sys
import urllib.request
import urllib.error
import json
import uuid
from base64 import b64encode

API = "https://api.close.com/api/v1"


def _auth_header(key):
    return "Basic " + b64encode(f"{key}:".encode()).decode()


def _post_json(url, payload, key):
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode(),
        headers={
            "Content-Type": "application/json",
            "Authorization": _auth_header(key),
        },
        method="POST",
    )
    with urllib.request.urlopen(req) as r:
        return json.load(r)


def _multipart(fields, file_field, filename, content, content_type):
    boundary = uuid.uuid4().hex
    body = b""
    for k, v in fields.items():
        body += (
            f"--{boundary}\r\nContent-Disposition: form-data; name=\"{k}\"\r\n\r\n{v}\r\n"
        ).encode()
    body += (
        f"--{boundary}\r\nContent-Disposition: form-data; name=\"{file_field}\"; "
        f"filename=\"{filename}\"\r\nContent-Type: {content_type}\r\n\r\n"
    ).encode()
    body += content + f"\r\n--{boundary}--\r\n".encode()
    return body, f"multipart/form-data; boundary={boundary}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lead-id", required=True)
    ap.add_argument("--png", required=True)
    ap.add_argument("--title", default="SSO grid 1")
    ap.add_argument("--note", default="", help="Platte tekst in de note zelf")
    args = ap.parse_args()

    key = os.environ.get("CLOSE_API_KEY")
    if not key:
        sys.exit("CLOSE_API_KEY staat niet in de omgeving.")

    path = args.png
    filename = os.path.basename(path)
    content_type = mimetypes.guess_type(filename)[0] or "application/octet-stream"
    with open(path, "rb") as f:
        content = f.read()

    # 1. signed upload aanvragen
    up = _post_json(
        f"{API}/files/upload/",
        {"filename": filename, "content_type": content_type},
        key,
    )

    # 2. naar S3 (geen auth-header, die hoort hier niet bij)
    body, ct = _multipart(
        up["upload"]["fields"], "file", filename, content, content_type
    )
    s3 = urllib.request.Request(
        up["upload"]["url"], data=body, headers={"Content-Type": ct}, method="POST"
    )
    try:
        with urllib.request.urlopen(s3) as r:
            if r.status not in (200, 201, 204):
                sys.exit(f"S3-upload gaf status {r.status}")
    except urllib.error.HTTPError as e:
        sys.exit(f"S3-upload mislukt: {e.code} {e.read().decode()[:400]}")

    # 3. note met bijlage
    note = _post_json(
        f"{API}/activity/note/",
        {
            "lead_id": args.lead_id,
            "note": args.note or args.title,
            "title": args.title,
            "attachments": [
                {
                    "url": up["download"]["url"],
                    "filename": filename,
                    "size": len(content),
                    "content_type": content_type,
                }
            ],
        },
        key,
    )
    print(json.dumps({"note_id": note.get("id"), "lead_id": args.lead_id}, indent=2))


if __name__ == "__main__":
    main()
