# Prompt voor een subagent (hele CRM)

Kopieer dit per groep leads. Vul de leads in met naam, lead_id, domein en de kandidaten uit `scan_dump.py` plus wat al in de repo staat. Model: Sonnet, `run_in_background`, 4 tegelijk.

---

Find the total number of students for these Close CRM leads. READ-ONLY: never create, update or delete anything in Close, Gmail, the repo or anywhere else.

First read the rules in `.claude/skills/studentenaantal/SKILL.md` and follow them exactly. Key points: only whole-organisation totals count (no pilot groups, cohorts, single programmes, intakes, staff, franchise partners, sister brands, or Eduface's own price tiers); source order is (1) what someone from the institution said in a recorded meeting or call transcript, (2) our own texts (Close notes, repo files) and emails in Close and Gmail, (3) online only official sources (registers, annual reports); rounded marketing claims on websites do not count; a customer's rough estimate only counts if no official figure differs from it by more than 25%. If nothing reliable: LEEG.

Leads:
1. <naam>, <lead_id>, <domein>. Known: <kandidaten uit de scan en de repo, met wat je al weet dat ze wel of niet zijn>.
2. ...

Per lead, in this order, and stop once you have a reliable answer:
a) Repo: `GTM/Accounts/<lead>/`, `GTM/sales-coach/data/deals/`, `GTM/ICP/shift/master/orgs.csv`, and `python3 .claude/skills/studentenaantal/scan_dump.py --lead "<naam>"`.
b) Close: load tools with ToolSearch ("select:mcp__Close__activity_search,mcp__Close__fetch_meeting_transcript,mcp__Close__fetch_call"). Check activity on the lead since the date of the local copy. Only open a transcript for a meeting that is in the local copy with a summary, or newer than the copy, and only if a student total seems to be mentioned. Large results get saved to a file: search them with grep or python instead of reading them whole.
c) Gmail: load "select:mcp__Gmail__search_threads" and search the lead's domain with studenten OR students (one search per lead).
d) Online, only if a to c gave nothing reliable: at most 3 lookups per lead, aimed at the register (DUO, HESA, IPEDS, SEC) or the annual report. A figure only counts if it clearly comes from that official source, with the reference year.

Report per lead in exactly this format (max 90 words per lead):
LEAD: name | lead_id
RESULT: number or LEEG
LEVEL: transcript | eigen tekst | mail | officieel | leeg
QUOTE: "verbatim sentence"
SOURCE: activity id / gmail thread id / file path / URL
SOURCE DATE: YYYY-MM-DD (and the reference year of the figure)
REJECTED: number, reason; ...
SEARCHED: where you looked (only if LEEG)
