# Session 1 run-of-show — Cowork 101: Documents, Transcripts, and Scheduled Tasks
Tuesday, October 6, 2026 · 6:00–7:30 PM CDT · Twin Ignition Startup Garage, Minneapolis · free · in person · recorded

Public promise (from the Meetup page): grant Cowork access to document folders; read and summarize meeting transcripts; set up recurring scheduled tasks. Audience: beginners and experienced Claude users. Laptop optional.

**Design rules for this room:** a prediction before every demo, one deliberate failure, three levels of try-along (Starter, Builder, Architect), and a handoff to next month. Nobody sits passive for more than 10 minutes.

## Clock

| Clock | Min | Block | You do | Room does |
|---|---|---|---|---|
| 5:00 | | Setup | AV test, kit link on slide, Wi-Fi/hotspot test, run Part 3 once so a digest exists | |
| 5:30 | | Doors | Helpers greet; QR on screen; pair anyone without a paid plan with a neighbor | Arrive, download kit |
| 6:00 | 7 | Welcome | Three promises. Recording notice. Pick a level. | Raise hands: Starter / Builder / Architect |
| 6:07 | 5 | One idea | The loop: Find, Do, Check, Repeat | Listen |
| 6:12 | 16 | Part 1: Documents | See below | Predict, grant folder, try |
| 6:28 | 24 | Part 2: Transcripts | See below | Try, catch the failure |
| 6:52 | 3 | Reset | Stand up. Helpers refill power strips and help stuck laptops | Stretch |
| 6:55 | 22 | Part 3: Scheduled task | See below | Create task, Run now |
| 7:17 | 13 | Wrap and Q&A | Homework, next month, how to get the recording | Questions into the mic |
| 7:30 | | Close | Stay for informal questions if the venue allows | |

Check: 7+5+16+24+3+22+13 = 90.

## 6:00 Welcome (7 min)
- "Tonight is the first lap of the loop. In six months we go from this to a team of automated processes you trust."
- Say out loud: this session is being recorded; slides and screen only; questions are repeated into the mic; step out of frame if you prefer. Everything shown is synthetic.
- Plans: "Cowork needs a paid plan. If you don't have one, you're in the best seat: sit with a neighbor."
- Level pick: Starter / Builder / Architect by show of hands. Helpers note where the Architects sit.

## 6:07 One idea (5 min)
**Cowork is Claude working inside your folders and on your schedule.** The loop: Find (what is in my files?), Do (turn it into something useful), Check (is it right?), Repeat (make it recurring). Tonight's three parts are the first three steps. Check and Repeat are the through-line to all six sessions.

## 6:12 Part 1: Documents (16 min)
1. **Predict (2):** "Write down 3 things you think are in the folder." Show the Birchwood story in one slide: 3 buildings, 76 units, a messy shared drive.
2. **Demo (4):** Grant access to `birchwood-folder`, run the Starter prompt, then the Builder index prompt. Point out the stale `OLD-late-notice...` file and the sticky notes.
3. **Try-along (7):** Everyone grants access and runs their level's prompt (`prompts/part-1-documents.md`).
4. **Reflect (3):** "What did Claude find that you didn't predict?" Take two answers.
- Key: `expected-outputs/03-cross-document-findings.md` items 2, 6, 7.
- Say: "The folder Claude can see is the folder it can quote."

## 6:28 Part 2: Transcripts (24 min)
1. **Demo (5):** Run the Starter prompt on the Sept 8 staff meeting. Read the action table aloud.
2. **Try-along (8):** Levels run their prompts. Architects try the three-transcript tracker.
3. **Failure moment (6):** On the Sept 8 transcript alone, ask: "What did the team decide about pet rent?" Show the answer. Ask the room: "Was anything decided?" (No: it was tabled.) Add the rule: "Quote the line; write 'not stated' if absent." Re-run. Then add Sept 15 and ask again (Cedar Point, new leases only).
4. **Cross-document (5):** Ask for the three-file tracker. Highlight the flags: boiler date moved, $620 over Marcus's limit, the unassigned 3B call.
- Key: `expected-outputs/02-decisions-key.md`, `05-planted-traps-and-prompts.md`.
- Say: "Claude is a fast reader, not a witness."

## 6:52 Reset (3 min)
Stand up and stretch. Helpers help anyone stuck. Presenter plugs power and checks the recording.

## 6:55 Part 3: Scheduled task (22 min)
1. **Concept (4):** "A scheduled task is a saved prompt plus a clock." Local versus cloud: a task that reads a folder on your computer runs on your computer, so the app must be open and the computer awake; tasks that use cloud connectors can run without it. Check this against your app version before Tuesday.
2. **Demo (5):** Create "Monday Action Digest" with the kit prompt, schedule it weekly, click Run now, open the digest.
3. **Try-along (8):** Everyone creates their own and runs it once. Builder adds the tracker comparison; Architect adds safety rules and the run log.
4. **History (3):** Open the digests seeded since Saturday on your machine: "This is what a week of unattended running looks like." Be honest about what it can't know ("no evidence of completion" is not "not done").
5. **If it fails (2):** open `expected-outputs/06-sample-monday-digest.md`.

## 7:17 Wrap and Q&A (13 min)
- Homework: pick one weekly task and fill in the process card (`prompts/homework.md`).
- Next session (early November, date TBD): capture a process as a reusable skill. Say where the Meetup page will announce it.
- How to get the recording and the kit (Drive link and GitHub).
- Q&A: repeat every question into the mic.
- Close with: "You now have three of the six steps. Month 2 turns your process card into something you can reuse."

## Backup plans
| If | Then |
|---|---|
| Wi-Fi fails for the room | Presenter on phone hotspot; attendees watch and pair; Part 3 sample digest is on the slide |
| Cowork is down or slow | Switch to the recorded dry run (make one on Sunday) and the sample outputs in `expected-outputs/` |
| Presenter laptop sleeps during Part 3 | You will know the lesson is true: say so, then run it |
| Many attendees without a paid plan | Pair them; offer to run prompts on request from the front |
| Running late | Cut the Architect try-along in Part 1; keep the failure moment |
