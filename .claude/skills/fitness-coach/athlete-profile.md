# Athlete Profile - Dante

Source of truth for the `fitness-coach` skill. Keep this current: when something changes (schema, maxes, InBody, WHOOP trends, goals), edit this file. Nutrition lives in `nutrition-profile.md`, the aesthetic layer in `physique-goal.md`, the full session detail in `reference/volledig_schema.html`.

**Last updated: 2026-08-29.** Big change this update: **football is over.** The old nickel/football program is archived in `archives/fitness-coach-football-2026-08/`. Don't coach off it anymore.

## Personal
- Born 2006 (19), based in Leiden, works at Eduface in Utrecht
- Commutes daily by train, **6:23 out of Leiden**. This sets the whole sleep window.
- Sunday field day is the only thing left from football

## Goal
**Greek god V-taper physique, lean bulk.** Not performance, not a sport. Build the top, keep the waist, add mass slowly enough that bodyfat stays near 10%. Full ratio targets in `physique-goal.md`.

## InBody (2026-08)

| Metric | Value |
|---|---|
| Weight | 89.4 kg |
| Bodyfat | 10.2% |
| Skeletal muscle mass | 46.8 kg |
| Lean body mass (derived) | ~80.3 kg |
| BMR (measured) | 2,104 kcal |

Lean at 89.4kg with 10.2% BF is a strong starting point. The job is adding muscle without letting bodyfat drift past ~12%, because bodyfat lands on the waist first and the waist is half the V-taper ratio.

## Lichaamsmaten (laatst 2026-09-05)

| Measurement | Value |
|---|---|
| Shoulders (circumference) | 120 cm |
| Chest | 101 cm |
| Waist | 79 cm |
| Hip | 102 cm |
| Bicep R / L | 38 / 37.5 cm |
| Upper leg R / L | 63.5 / 62.5 cm |

Schouder/taille-ratio **1.52**, doel 1.6+. Ongewijzigd sinds 05-07-2026: alle acht de maten zijn exact gelijk gebleven over twee maanden.

**Alle metingen staan in `projects/fitness/data/metingen/metingen.csv`.** Dat is de historie, dit tabelletje is alleen de laatste stand. Nieuwe meting? Regel eronder plakken, niet dit bestand overschrijven. Tapemeting elke 4-6 weken, 's ochtends, ontspannen, niet gepompt. InBody wekelijks op zondag.

## Weekly schedule

| Day | Session |
|-----|---------|
| Monday | Rest |
| Tuesday | Gym - **Lower B** (hack squat, RDL, Bulgarian) |
| Wednesday | Rest |
| Thursday | Gym - **Upper A** |
| Friday | Rest |
| Saturday | Gym - **Lower A** (squat, leg ext, seated leg curl, hip thrust) |
| Sunday | Gym - **Upper B** + field day |

Rotation is **lower / upper / lower / upper**, so Sunday's gym session is upper body and does not collide with field day. Every muscle group still gets hit 2x/week. Field day stays Sunday, fixed.

Why Lower B sits on Tuesday and not Saturday: **Lower B contains the RDL**, a loaded hamstring stretch. Sprinting on hamstrings that are sore from RDLs is the single most common way to tear one. Lower A's hamstring work is the seated leg curl, which is far safer to sprint on the next day. So the heavier hip-hinge day goes as far from field day as possible.

Leg spacing is Tue -> Sat (4 days) and Sat -> Tue (3 days). Fine for 2x/week.

## Gym schema (summary - full detail in `reference/volledig_schema.html`)

Every session ~70-80 min, with a 3-5 min dynamic warm-up and loaded warm-up sets before the first compound. Rest: warm-up sets 60-90s, compounds 2-3 min, isolation 90s-2 min, calves 60-90s.

### Upper A - flat chest, pull-up, shoulders, triceps long head, proximal biceps
1. Bench Press (BB) 2x6-8
2. Weighted Pull-Up 3x4-6 (+15-20kg)
3. Lateral Raise (DB) 3x dropset (15 -> -30% -> 12 -> -30% -> 10)
4. Chest-Supported Row (DB) 2x10-12
5. Overhead Triceps Extension (cable) 2x10-12
6. Incline Curl (DB, one arm) 2x10-12
7. Reverse Fly (cable) 2x12-15
8. Ab Wheel 2x max

### Upper B - upper chest (30 deg), lat pulldown, shoulders, distal biceps, lower abs
1. Incline DB Press 30 deg, 2-3x8-10
2. Lat Pulldown 3x8-10 (grip ~1.5x shoulder width)
3. Lateral Raise (DB/cable) 3x dropset
4. Chest-Supported Row 2-3x10-12
5. Preacher Curl (DB, one arm) 2x10-12
6. Triceps Pushdown 2x12-15
7. Rear Delt Fly 2x12-15
8. Hanging Leg Raise 2x max

### Lower A - squat, leg extension, seated leg curl, hip thrust, calves
1. Back Squat, parallel or deeper, 3x4-6
2. Leg Extension, seat reclined ~40 deg, 3x10-12
3. Seated Leg Curl 3x10-12 (seated only, never lying)
4. Hip Thrust (BB) 2x8-10
5. Standing Calf Raise 3x15-20
6. Seated Calf Raise 2x15-20

### Lower B - hack squat, RDL, Bulgarian split squat, calves
1. Hack Squat 3x8-10
2. Romanian Deadlift 3x8-10 (to just below the knee, not the floor)
3. Bulgarian Split Squat 2-3x10-12
4. Standing Calf Raise 3x15-20
5. Seated Calf Raise 2x15-20

## Field day - Sunday (~60 min)
Kept from the football program because he likes it and it burns strain without adding hypertrophy fatigue. Now it's conditioning and athleticism, not position prep.
1. Warm-up 10 min: dynamic mobility, A/B skips 2x20m, build-up sprints 3x30m
2. Ladder and footwork 10 min
3. Plyometrics 12 min: broad jumps 4x3, box jumps 4x5, lateral box jumps 3x5/side. Reactive bounce for broad and lateral, static reset for standard box jumps.
4. Sprints 12 min: resisted 4x20m, free 100% 4x30m, 90s rest
5. Agility 12 min: backpedal + open hips, W-drill, plant and cut, lateral slides
6. Finish 4 min: one full-field sprint, 3 min cooldown walk

## Werkgewichten (Strong-export t/m 2026-08-15, 476 workouts sinds 2021)

Ruwe export: `projects/fitness/data/strong/strong_workouts.csv`. Zwaarste set sinds mei 2026:

| Oefening | Beste set | Laatst gelogd |
|---|---|---|
| Bench Press (BB) | 110 kg x2 | 2026-07-20 |
| Squat (BB) | 120 kg x2 | 2026-08-15 |
| Trap Bar Deadlift | **160 kg x8** | 2026-07-16 |
| Pull Up | +20 kg x3 | 2026-07-20 |
| Pendlay Row | 70 kg x3 | 2026-07-20 |
| Push Press | 60 kg x2 | 2026-07-17 |
| Overhead Press (BB) | 60 kg x5 | 2026-06-22 |
| Incline DB Press | 42 kg x4 | 2026-07-07 |
| One Arm DB Row | 36 kg x8 | 2026-07-13 |
| Lateral Raise (kabel) | 16 kg x15 | 2026-08-13 |
| Triceps Extension (kabel) | 34 kg x12 | 2026-07-17 |
| Standing Calf Raise | 65 kg x15 | 2026-08-15 |
| Bulgarian Split Squat | 28 kg x8 | 2026-06-24 |

**Correctie:** het oude profiel noemde een trap bar deadlift van 65 kg met een vraagteken. Dat was een opwarmset. Werkelijk 160 kg x8.

**Geen historie voor de nieuwe oefeningen.** Hack squat, seated leg curl, preacher curl, chest-supported row en RDL staan niet in de Strong-export. Eerste weken zijn dus inschatten: begin conservatief en laat hem de eerste sessie zelf inschieten, programmeer er geen percentages op.

Laatste gelogde workout is 2026-08-15, het nieuwe schema is daarna ingegaan.

## Wekelijkse upload (zondag)

Elke zondag levert hij drie dingen aan: **Strong-export, WHOOP-export en InBody-uitslag.** Die gaan naar `projects/fitness/data/`.

Dat is **context voor de coach, geen dashboardinhoud.** Hij heeft de WHOOP-app al om zijn WHOOP-cijfers te bekijken en hoeft ze niet nog een keer te zien. Gebruik de data om vragen te beantwoorden en het weekmenu en het schema bij te stellen, en bouw er geen tegels van.

## WHOOP baselines (export 2026-08-24, 237 cycles from 2025-01-08)

| Metric | All-time | Last 90 days |
|---|---|---|
| Recovery | 59.1% | 57.1% |
| HRV | 41.1 ms | 42.0 ms |
| Resting HR | 63.5 bpm | 60.1 bpm |
| Sleep performance | 65.6% | 65.7% |
| Asleep | 6.35 h | **6.14 h** |
| Sleep consistency | 60.6% | 60.3% |
| Day strain | 10.5 | 10.4 |
| Energy burned | 2,396 cal | 2,307 cal |

**Only 3 of the last 23 logged nights hit 8 hours.** Sleep debt sits pinned near the 127 min ceiling.

Sleep and recovery by weekday (since 2026-05-01):

| Day | Asleep | Sleep perf | Recovery | Strain |
|---|---|---|---|---|
| Mon | 5.41 h | 60.5% | 62.3 | 7.5 |
| Tue | 7.08 h | 76.7% | 67.0 | 11.4 |
| Wed | 6.72 h | 71.7% | 54.2 | 13.2 |
| Thu | 6.20 h | 65.0% | 46.3 | 11.6 |
| Fri | 6.01 h | 68.1% | 55.4 | 10.7 |
| Sat | 6.34 h | 64.0% | 55.3 | 17.0 |
| Sun | 6.12 h | 57.4% | 59.4 | 9.3 |

Read: **Sunday night into Monday is the worst sleep of the week (5.4 h)**, and Thursday is the worst recovery (46%). With football gone, the late-night cap on sleep is gone too, so this is now fixable rather than structural.

## Recovery adjustment rule (football version, kept)
- Green (67%+): full intensity as planned
- Yellow (34-66%): -1 set per exercise, top sets -5 to -10%
- Red (0-33%): drop the heavy compound to 3x8 at 70%, keep the isolation work
- HRV down 3 days running: turn the next session into an Upper B-style pump session or take the rest day

## Supplements
- Creatine 5 g daily, every day, no loading
- Fish oil and multivitamin logged most days in WHOOP journal
- Compression therapy is logged 28 times and answered **yes 0 times**. Either stop tracking it or start doing it.

## Daily morning stretch (12-15 min, unchanged)
- Hip and lateral: 90/90 60s/side, pigeon 60s/side, adductor squat hold 45s, world's greatest 5/side
- Thorax and shoulders: open book 10/side, thoracic rotation on roller 10/side, doorway pec 45s/side
- Gym days add: lateral leg swings 10/side, hip circles 10/side, band pull-aparts 2x15, deep squat hold + rotation

Neck block is optional now. It was a defensive-back requirement, not a V-taper one, and a thicker neck does nothing for the taper.

## Open flags (raise these, don't silently work around them)
1. ~~Sunday doubles up Lower B and field day.~~ **Resolved 2026-08-29:** rotation flipped to lower/upper/lower/upper, so Sunday is Upper B + field day. Field day stays Sunday. Remaining watch item: Saturday's Lower A the day before field day still leaves quads a bit fresh-sore for sprints. If sprint quality drops, cut Saturday's leg extension by a set rather than moving the day.
2. **3,100 kcal vs WHOOP's 2,307 measured burn.** WHOOP consistently underestimates, and BMR 2,104 x 1.5 activity puts real TDEE around 3,150. 3,100 is therefore roughly maintenance to a small surplus, which is right for a lean bulk. But it is an estimate, so steer on the scale, not the calculator. See `nutrition-profile.md`.
3. **Sleep is the bottleneck for the whole plan.** 6.14 h will not support a lean bulk at 175-180 g protein. Fixing sleep is worth more than any program change.
4. Trap bar and power clean are gone with football. No need to sanity-check that old 65 kg trap bar number anymore.
