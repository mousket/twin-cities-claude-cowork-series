# Cowork 101 — Session plan (follow it live or on your own)

**Twin Cities Claude & Agentic AI Meetup · Session 1**

This is the whole session in one page. In the live meetup it runs 90 minutes with a presenter. At home you can go at your own pace. Estimates for working alone: one or two parts take about 45 minutes; all three parts with the harder prompts take about 90.

Everything in `birchwood-folder/` is synthetic. Birchwood Property Group, its people, tenants, vendors and numbers are invented.

## What you will have at the end
1. Given Cowork access to one folder, and seen what it can find in it.
2. Turned meeting transcripts into decisions and action items, and caught Claude in a mistake.
3. Created a scheduled task that writes a weekly digest, and run it once.
4. A process card for one task of your own (homework).

## Before you start (about 10 minutes)
Do the checks in `before-you-start/01-before-you-start.html` (open it in any browser). The short version:

| You need | Required? |
|---|---|
| Internet connection | Required |
| A Mac (macOS 11+) or Windows (10+) computer | Required for hands-on |
| A web browser | Required |
| A paid Claude plan (Pro, Max, Team or Enterprise). Cowork is not on the Free plan | Required for hands-on |
| The Claude desktop app, up to date | Required for hands-on |
| VS Code (free) to read the kit's Markdown, CSV and text files | Recommended |
| A GitHub account, or a Google account for Drive | Recommended |

No paid plan or no computer? You can still read the plan, read the files in VS Code, and follow along by watching. Pair with someone if you are at the live meetup.

## The one rule
Connect **only** the `birchwood-folder` folder to Cowork. Never give it your real Documents, Desktop or Downloads folders during these exercises.

## The idea: Find, Do, Check, Repeat
Cowork is Claude working inside your folders and on your schedule. The loop:

- **Find:** what is in my files?
- **Do:** turn it into something useful.
- **Check:** is it right?
- **Repeat:** make it recurring.

Tonight's three parts are the first three steps. Check and Repeat run through every session in the series.

## Pick a level (switch any time)
- **Starter:** one useful result.
- **Builder:** a result you would trust, with evidence and checks.
- **Architect:** a result that survives being run again.

## Timeline (minutes from the start)

| From | Block | What you do |
|---|---|---|
| 0:00 | Welcome | Pick a level |
| 0:07 | One idea | Read the loop above |
| 0:12 | Part 1: Documents | About 16 min |
| 0:28 | Part 2: Transcripts | About 24 min |
| 0:52 | Stretch | Stand up for three minutes |
| 0:55 | Part 3: Scheduled task | About 22 min |
| 1:17 | Wrap up | Homework, next session |
| 1:30 | Close | |

## Part 1 — Documents (about 16 min)
Prompts: `prompts/part-1-documents.md`.

1. **Predict (2 min).** Before you grant access, write down three things you think are in `birchwood-folder`. It is a messy shared drive for 3 buildings and 76 units.
2. **Grant access and run your level's prompt (about 10 min).** In Cowork, choose `birchwood-folder` as the folder. Run the Starter prompt, then Builder or Architect if you want more.
3. **Reflect (3 min).** What did Claude find that you didn't predict? Look at the files it flagged and open them in VS Code to check.

**Remember:** the folder Claude can see is the folder it can quote.

## Part 2 — Transcripts (about 24 min)
Prompts: `prompts/part-2-transcripts.md`. Transcripts are in `birchwood-folder/meeting-transcripts/`.

1. **Starter prompt on the Sept 8 staff meeting (about 8 min).** Read the action table Claude gives you. Open the transcript and check two rows against it.
2. **Catch a mistake (about 8 min).** On the Sept 8 transcript alone, ask: "What did the team decide about pet rent?" Before you trust the answer, find the lines about pet rent in the transcript and decide for yourself whether anything was actually decided. Then add this rule and ask again: "Quote the line where it was decided. If it isn't stated, write 'not stated'." Compare the two answers.
3. **Add another meeting (about 5 min).** Add the Sept 15 owner call and ask the same question again. Notice what changed and why.
4. **Cross-document (about 3 min, Builder and Architect).** Run the tracker prompt across all three transcripts. Look for things that moved, things that conflict with a policy, and things with no owner.

**Remember:** Claude is a fast reader, not a witness. Predict, ask for the evidence, then check.

## Stretch (3 min)
Stand up. Drink some water.

## Part 3 — A scheduled task (about 22 min)
Prompts: `prompts/part-3-scheduled-task.md` and `prompts/scheduled-task-prompt.md`.

1. **The concept (about 4 min).** A scheduled task is a saved prompt plus a clock. A task that reads a folder on your computer runs on your computer, so the Claude app must be open and the computer awake when it fires. Check how your version of the app describes this.
2. **Create it (about 8 min).** In the Claude desktop app, open **Scheduled** in the sidebar and start a new task (the exact labels may differ in your version). Name it **Monday Action Digest**. Paste the prompt from `prompts/scheduled-task-prompt.md`. Choose a weekly frequency and your working folder, then run it now.
3. **Open what it wrote (about 5 min).** Look in `birchwood-folder/digests/`. Check two items in the digest against the transcripts.
4. **Level up (about 5 min).** Builder: compare with `data/action-tracker.csv`. Architect: add a safety rules block and a run log.

**Honest note:** a digest can say "no evidence of completion". That is not the same as "not done". Decide what you would do with it before you trust it unattended.

## Wrap up (about 13 min live, 5 min alone)
- **Homework** (about 30 minutes before Session 2): fill in the process card in `prompts/homework.md` for one task you repeat every week. Time yourself doing it once by hand. Do not automate it yet.
- **Next session:** capture a process as a reusable skill. Watch the Meetup page for the date.

## If something goes wrong
| Problem | What to try |
|---|---|
| You don't see Cowork in the app | Update the desktop app, restart it, confirm you're signed in to a paid plan |
| You can't choose a folder | Put the kit in Documents and try again; allow the folder when your computer asks |
| Claude says you've reached a usage limit | Wait for it to reset, or do the parts on a later day |
| The kit looks wrong or a file changed | Delete the `birchwood-starter-kit` folder and unzip the original zip again |
| Claude's answer disagrees with the transcript | That's the lesson. Quote the line, ask again with the rule, and trust the file, not the confidence |

## What to try next with your own material
Only after you've done the exercises. Choose a small folder with non-sensitive files, connect only that folder, and ask Claude the Part 1 question. Never connect a folder with client, tenant or employee data unless you have the right to share it with Claude.

Source of facts about Cowork: Anthropic's support pages (checked October 2, 2026). Labels and menus change, so trust your screen.
