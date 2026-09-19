# Context Loading — Work vs Personal

Keep work and personal context separate. Don't mix them, and don't waste tokens loading the wrong one.

## Work (default)
- Work context lives in `@context/me.md`, `@context/work.md`, `@context/team.md`, `@context/current-priorities.md`, `@context/goals.md`. These auto-load every session.
- For work tasks, stay in work context only. Do not pull in personal context.

## Personal (on demand)
- Personal context lives in `context/personal.md`. It is **intentionally NOT auto-imported**, so it never loads during work sessions.
- Only read `context/personal.md` when the task is genuinely personal (e.g. gym/health, personal admin).
- When working on personal tasks, keep work context out of it.
