#!/bin/zsh
# Eduface daily automation - ONE headless Claude session per run (keeps the conversation list tidy).
# Does two read-only tasks: (1) hot-lead outreach draft step, (2) webinar HHS aanmeld-sync (self-expires after 2026-06-24).
# Phase 1: draft + queue to Todoist only. NEVER sends. Send tools stay gated in .claude/settings.json (ask).
set -u

PROJECT="/Users/User/Library/CloudStorage/GoogleDrive-dante.torbed@eduface.me/My Drive/Eduface/Claud AE"
LOG="$HOME/Library/Logs/eduface-hotleads.log"

# Resolve the newest bundled claude binary from the VSCode extension (survives version bumps).
CLAUDE=$(ls -dt "$HOME/.vscode/extensions/anthropic.claude-code-"*/resources/native-binary/claude 2>/dev/null | head -1)

mkdir -p "$HOME/Library/Logs"
echo "===== $(date '+%Y-%m-%d %H:%M:%S') run start =====" >> "$LOG"

if [ -z "$CLAUDE" ] || [ ! -x "$CLAUDE" ]; then
  echo "ERROR: claude binary not found under ~/.vscode/extensions" >> "$LOG"
  exit 1
fi

cd "$PROJECT" || { echo "ERROR: cannot cd into project (Drive unmounted?)" >> "$LOG"; exit 1; }

# Single prompt = single Claude session per run. Both tasks are read-only on Lemlist.
PROMPT="You have read-only daily tasks below. Do them in order. Hard rules for all tasks: use Lemlist call_api with GET only, NEVER POST, never send, never add leads to campaigns, never change campaign state, never delete anything.

TASK 1 - Hot lead outreach, draft step. Run the hot-lead-outreach skill (.claude/skills/hot-lead-outreach/SKILL.md). Find new hot leads in Lemlist campaigns cam_Ss9Es6ayPFtGAtiNa and cam_3vg5T7GS4qNqXyoxP. Filter to hot: LinkedIn invite accepted, email opened, no reply (Lemlist does not expose a usable lead score, so qualify on engagement signals). Dedupe against Todoist project 6gqR7Q5Gj9MgjVVg by lead ID (task footer carries 'Lead: lea_xxx'). For each NEW lead only, create one Todoist review task with the LinkedIn DM + email drafts per the skill tier logic. Draft and queue only."

# Webinar sync only runs up to and including the webinar window (23 June 2026).
if [[ "$(date +%Y%m%d)" -le 20260624 ]]; then
  PROMPT="$PROMPT

TASK 2 - Webinar HHS aanmeldingen sync. In Lemlist campaign cam_S6jGvg6hMDwXJ3dpk list pending manual tasks via get_tasks (campaignId cam_S6jGvg6hMDwXJ3dpk, type manual) - each pending manual task is a lead who clicked the aanmeldlink. Dedupe against Todoist project 6gqRR6gxjxr7FCpx (each existing task footer carries a 'Lead: <email>' line). For each NEW clicker only, add one Todoist task in project 6gqRR6gxjxr7FCpx titled 'Check aanmelding: <firstName> <lastName> (<companyName>)' with description 'Klikte op de aanmeldlink. Check in Teams of diegene zich heeft aangemeld. Zo ja: voeg toe aan bedank-campagne cam_ExwBJpZ5h5mQTvMjq en vraag om collega's uit te nodigen. Zo nee: zet terug op de reminder.' and on a final line 'Lead: <email>'."

  PROMPT="$PROMPT

TASK 3 - Webinar replies, supervised draft only. List Lemlist unread inbox conversations via get_inbox_conversations listId unRead. For each conversation whose lead is in campaign cam_S6jGvg6hMDwXJ3dpk (verify against that campaign leads via search_campaign_leads; skip leads from other campaigns), read the thread via get_inbox_conversation with markAsRead false (do NOT mark read). Classify and act: (a) out-of-office or autoreply: skip, no task. (b) negatief of geen interesse of stop: Todoist task in project 6gqRcf77j2PrvRP6 titled 'Reply nee: <firstName> <lastName>' description 'Negatieve reply, schrijf uit in Lemlist.'. (c) kan niet komen of wil de opname: task in 6gqRcf77j2PrvRP6 titled 'Reply opname: <firstName> <lastName>' description 'Wil de opname, sturen na 23 juni.'. (d) interesse of vraag of doorverwijzing: task in 6gqRcf77j2PrvRP6 titled 'Reply actie: <firstName> <lastName> (<companyName>)', quote in de description de reply van de lead en schrijf een klaar-om-te-versturen Nederlands antwoord in Eduface-stijl (casual, geen em-dashes, kort; CRO-logica: een positieve reply is een pijplijn-opening, duw naar deelname plus een kort gesprek; beantwoord vragen direct; bij doorverwijzing een korte intro naar de genoemde collega). Dedupe alle reply-taken tegen project 6gqRcf77j2PrvRP6 op de 'Lead: <email>'-footer, een open taak per lead, en sluit elke reply-taak af met een regel 'Lead: <email>'. SUPERVISED: alleen concept, nooit zelf versturen, nooit uitschrijven. Dante keurt goed en verstuurt."
fi

PROMPT="$PROMPT

End with a one-line summary per task. For an empty task say 'No new ... today.'"

"$CLAUDE" -p "$PROMPT" \
  --model sonnet \
  --permission-mode bypassPermissions \
  --output-format text >> "$LOG" 2>&1
RC=$?

# Tidy old run transcripts: 5-day retention. Shell-only, spawns NO Claude session.
# Only touches *.jsonl files and UUID-named sidecar dirs; never the memory/ folder or the active (today's) chat.
TRANSCRIPTS="$HOME/.claude/projects/-Users-User-Library-CloudStorage-GoogleDrive-dante-torbed-eduface-me-My-Drive-Eduface-Claud-AE"
if [ -d "$TRANSCRIPTS" ]; then
  PRUNED=$(find "$TRANSCRIPTS" -maxdepth 1 -name "*.jsonl" -mtime +5 2>/dev/null | wc -l | tr -d ' ')
  find "$TRANSCRIPTS" -maxdepth 1 -name "*.jsonl" -mtime +5 -delete 2>/dev/null
  find "$TRANSCRIPTS" -maxdepth 1 -type d -name "????????-????-????-????-????????????" -mtime +5 -exec rm -rf {} + 2>/dev/null
  echo "$(date '+%Y-%m-%d %H:%M:%S') pruned $PRUNED transcript(s) older than 5 days" >> "$LOG"
fi

echo "===== $(date '+%Y-%m-%d %H:%M:%S') run end (exit $RC) =====" >> "$LOG"
exit $RC
