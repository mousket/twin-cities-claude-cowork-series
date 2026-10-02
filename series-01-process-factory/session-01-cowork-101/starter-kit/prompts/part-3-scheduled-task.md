# Part 3 — A scheduled task that writes the Monday digest

Important to know before you start:
- A task that reads a folder on your computer runs **on your computer**. It needs the Claude app open and your computer awake when it fires. Tasks that use cloud connectors instead can run without your computer; we will talk about the difference live.
- The exact menu names may differ in your version of the app. If you don't see "Scheduled tasks," ask Claude in your task to help you find where scheduling lives.

## Starter
Create a scheduled task named **Monday Action Digest** that runs weekly on Monday mornings. Paste the prompt from `prompts/scheduled-task-prompt.md`. Then run it once now and open the file it wrote in `digests/`.

## Builder
Add this to the end of the prompt, then run it again:
> Compare your findings with `data/action-tracker.csv`. Don't list items already marked Done. List new items first.

## Architect
Add a safety rule block to the prompt (what it must never do, when it should stop and ask), plus a line that appends one row per run to `digests/run-log.csv` with the date, the files it read, and the number of items found. Run it twice and check the log.

**Reflect:** what would make you trust this running while you're on vacation?
