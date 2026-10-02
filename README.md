# Cowork Seminars

Materials for the Twin Cities Claude & Agentic AI Meetup's Claude Cowork series (automation and scheduled processes for developers and business owners).

Everything in `synthetic-data/` is fictional. Nothing here is legal or financial advice.

## Layout
- `series-01-process-factory/`: six monthly sessions, each with `instructions/`, `synthetic-data/`, `deck/`, `starter-kit/`, `homework/`, `recording/`
- `_shared/`: scenarios, templates, day-0 checklist, reference
- `scripts/make_kit.py`: builds the attendee zip

## Session 1: Tuesday, October 6, 2026
Cowork 101: Documents, Transcripts, and Scheduled Tasks. Start at `series-01-process-factory/session-01-cowork-101/README.md`.

## Building the attendee kit
```
python3 scripts/make_kit.py
```
Creates `birchwood-starter-kit.zip` beside the script's parent folder. It contains the starter-kit documents and the synthetic input files, never the answer keys.

## Before you make this repository public
`expected-outputs/` and `instructions/` are instructor material. Decide whether to publish them before or after the session. There is no license file yet; choose one deliberately.
