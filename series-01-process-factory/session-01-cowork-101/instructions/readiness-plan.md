# Session 1 readiness plan: Cowork 101

**Session:** Tuesday, October 6, 2026, 6:00 to 7:30 PM CDT · Twin Ignition Startup Garage, Minneapolis · free · recorded
**Written:** Monday, October 5, about noon. Roughly 30 hours to the start.

Everything the session needs, in the order you asked for it, with an honest status on each item and a schedule for today and tomorrow.

**Status key:** DONE = built and checked here. BUILT = exists but not yet tested by a human on a clean machine. TODO = still to do. UNKNOWN = I can't see it from here, so tick it yourself.

## 0. The honest read (start here)

**What is solid.** The session design, the run-of-show, the starter kit (29 files, including the participant plan), the answer keys, the prompts, the pre-session pages, and the three promotion drafts all exist.

**What is not done, and matters most.**
1. **Nobody can get the kit yet.** As of the last time I looked, there was no GitHub Release and no Drive link. If attendees can't reach the kit, the pre-session work is pointless. This is the first thing to fix today.
2. **The pages are private.** The two published pages are visible only to you until you share them, and I haven't verified that people without a Claude account can open them. Test in a private window.
3. **The session has never been run end to end.** The prompts and answer keys were built carefully, but no human has run all three parts on a stopwatch with the real kit, in the real Cowork app. Menu labels, folder-picker steps and approval prompts are unverified. A rehearsal is the single best use of your afternoon.
4. **There is no speaker script and no slides.** The run-of-show is a good skeleton, but you'd be improvising the words. For 30 to 50 people you want the first 7 minutes and the last 5 written out.
5. **You'll be spending your own usage allowance.** Cowork uses more allowance than chat. A full rehearsal today plus the live session tomorrow could hit your limit. Check your usage before you rehearse, and plan to do one full run today and only light checks tomorrow.

**What I can't see (tick or tell me):**
- [ ] Meetup update (paid plan, recording, links) sent?
- [ ] Saturday's sleep test run? What happened with the lid closed?
- [ ] Release `session-01` created? Drive link made?
- [ ] Venue answers (Wi-Fi, AV, mic, power, setup time)?
- [ ] Helpers confirmed? (Need 3: two floaters and a recorder/timekeeper.)

## 1. Plan the workshop

### What people get and accomplish by 7:30

| By the end, each person has | How they know |
|---|---|
| Given an AI access to one folder and seen what it found, including things they didn't predict | They wrote three predictions at the start and compared |
| Turned three meetings into decisions and action items, and caught Claude getting something wrong | They saw "tabled" reported as "decided" and fixed it with a rule |
| Created a scheduled task that writes a Monday digest, and run it once | A digest file exists in `digests/` |
| A process card for one real weekly task of their own | They filled it in as homework |
| Four habits | Predict first. Ask for the evidence. Allow "not stated". Give a rule and test it |

**They take home:** the starter kit, `SESSION-PLAN.md` (the whole session, step by step), the prompts at three levels, the Before You Start and Get the Kit pages, the glossary, and the recording.

**They do not leave with:** a production automation, a guarantee of hours saved, or permission to connect real client data. Say that out loud. It builds trust.

### The business-owner lens

The one-sentence promise for the whole session: **AI carries the load of remembering, finding and following up, so people have more time and less stress for the work only they can do.** Every block should answer three questions: what stress does this remove, what time does it give back, and what does a person still own?

| Block | The stress it removes | The time it gives back | What a person still owns |
|---|---|---|---|
| Part 1: Documents | "Where's that file, and which version is current?" | Searching and re-reading | Deciding which file is the real policy; checking what Claude flagged |
| Part 2: Transcripts | Meetings where nobody wrote down who is doing what | Writing up notes; chasing follow-ups | Deciding what was actually decided; confirming the owner; quoting the line |
| Part 3: Scheduled task | Remembering to do the Monday follow-up | The weekly summary writes itself | Acting on the digest; deciding what the task may and may not do |
| Homework | A vague "I should automate something" | A measured baseline in minutes | Choosing which task is worth it |

**Do not promise numbers.** We don't know how many hours this saves anyone. The homework process card measures it, which is the honest answer.

**Cast from the room's point of view:** Dana (operations manager) is the person in the audience. She is not short of tools. She's short of attention. Everything we show is about giving it back.

## 2. Create the plan: the documents

| Item | Where | Status |
|---|---|---|
| 90-minute run-of-show (presenter) | `instructions/run-of-show-90min.md` | DONE |
| Participant plan, usable live or at home | `starter-kit/SESSION-PLAN.md` | DONE (also inside the kit) |
| Prompts at three levels, plus homework | `starter-kit/prompts/` | DONE |
| Answer keys and planted traps | `synthetic-data/.../expected-outputs/` | DONE (public in the repo) |
| Room and recording checklist | `instructions/room-and-recording-checklist.md` | DONE, venue answers UNKNOWN |
| Attendee messages | `instructions/attendee-message.md` | DONE, links to fill in |
| Gotchas log | `instructions/gotchas-log.md` | TODO: create it during rehearsal |
| **Slides** | `deck/` | **TODO** |
| **Speaker script** | `instructions/speaker-script.md` | **TODO** |
| Apply the business-owner lens to the run-of-show | `instructions/run-of-show-90min.md` | TODO (about 20 minutes, see section 5) |

**The minimum deck (9 slides is enough):**
1. Title, plus the QR code for the kit
2. What you'll leave with (the four outcomes above)
3. The loop: Find, Do, Check, Repeat
4. Meet Birchwood Property Group: 3 buildings, 76 units, one Monday morning
5. Part 1: the prediction prompt, and "the folder Claude can see is the folder it can quote"
6. Part 2: the rule ("Quote the line. Write 'not stated' if absent")
7. Part 3: "A scheduled task is a saved prompt plus a clock," and the honest note about the app being open
8. Homework: the process card
9. Next session, the recording, the kit link and QR

## 3. Run through the plan: the rehearsal

**Do this once, fully, today.** Not "skim it". The point is to find what's wrong while there is still time to fix it.

**Setup (10 minutes):**
1. Download the kit exactly as an attendee would (from the Release, not from your repo). Unzip it to a clean folder.
2. Make sure you're on the same account, plan and app version you'll use tomorrow. Check your usage allowance first.
3. Start a stopwatch and a screen recording. Keep a notes file open (`instructions/gotchas-log.md`).

**Run it (about 90 minutes):** Part 1, Part 2 including the pet-rent failure moment, Part 3 including Run now. Say your lines out loud.

**Write down, with timestamps:**
- Every menu label that differs from the guides (folder picker, Scheduled, approval prompts). Send them to me and I'll correct the pages and the plan.
- Anything that took longer than the run-of-show allows.
- Whether the pet-rent trap behaves as the answer key says. If Claude gets it right the first time, say so and decide how you'll teach the lesson anyway.
- What happens when you click Run now on the scheduled task, and what the digest looks like.
- Anything that made you hesitate. Those are the moments the room will hesitate too.

**Pass criteria:** all three parts complete inside the time boxes (or you know what to cut), no surprise prompts you can't explain, a digest file you're happy to show.

**Second pair of eyes (30 minutes, worth it):** have one other person, ideally on Windows or a different Mac, do Before You Start and the kit download cold. Watch where they stall.

**The sleep test.** The "does the task run with the lid closed" question is still open unless you ran it Saturday. If you did, write down what you saw, with times. If you didn't, **don't make claims about it tomorrow**. Say: "A task that reads files on your computer runs on your computer. Keep the app open and the machine awake." That is what Anthropic's documentation says, and it's safe.

## 4. Create the script

Status: TODO. This is the biggest gap and the best use of my time next.

**Shape:** word for word for the opening (first 7 minutes), the two transitions, the failure moment, and the close (last 5 minutes). Bullets with cue lines for the try-along stretches.

**The 10 lines to know without notes:**
1. Who you are, and why Cowork.
2. The one-sentence promise (the business-owner lens above).
3. The recording notice and the out-of-frame option.
4. "Pair up if you don't have a paid plan. You're in the best seat."
5. The loop: Find, Do, Check, Repeat.
6. "The folder Claude can see is the folder it can quote."
7. "Claude is a fast reader, not a witness."
8. The scheduled-task honesty line (app open, computer awake).
9. The homework ask.
10. The close: "You now have three of the six steps."

## 5. Check the business-owner lens on the whole session

Read the run-of-show once with these questions, block by block.

- [ ] Does the welcome open with the owner's problem (too much in your head, too little time) rather than the tool?
- [ ] Does each part end with "what a person still owns"?
- [ ] Does the Part 2 failure moment say out loud why it matters to a business: a decision that was never made gets acted on?
- [ ] Does Part 3 end with "what would make you trust this while you're on vacation?"
- [ ] Does the close come back to time and stress, not features?
- [ ] Do we avoid promising hours saved?
- [ ] Is every example in the kit fictional, with no real names, tenants or numbers?

## 6. Finish the pre-session project

| Item | Status | Next step |
|---|---|---|
| Before You Start page | DONE, republished | Share it, test in a private window |
| Get the Starter Kit page | DONE, republished | Share it, test in a private window |
| Kit zip (29 files, includes SESSION-PLAN.md) | BUILT | Create the Release with it (below) |
| Repo copies of both pages, README and PUBLISHED.md | BUILT | Unzip `cowork-update-4-before-you-start.zip`, `git rm` the old `01-before-you-come.html`, commit, push |
| GitHub Release `session-01` | **TODO** | `gh release create session-01 birchwood-starter-kit.zip --title "Session 1 starter kit" --notes "Cowork 101. Everything in the kit is fictional."` |
| Google Drive copy | TODO | Upload the same zip, set "Anyone with the link can view", send me the link and I'll add it to the pages |
| Test the links as a stranger | TODO | Private window, signed out of everything. Open both pages, download the kit from the Release |
| Meetup update | UNKNOWN | Send `attendee-message.md` section 1 with the real links, plus the paid-plan note and the recording notice |
| Update the event description on Meetup | TODO | Add the paid-plan requirement and the kit link |
| Optional "Ready?" poll | TODO | Tells you how many pairs and helpers to plan for |
| Printed `START-HERE.md`, 10 copies | TODO | Print Tuesday morning |
| USB sticks with the kit | optional | The cheapest insurance against bad Wi-Fi |

**Release is required, Drive is optional.** If Drive slips, ship with the Release alone. Don't hold the Meetup update for it.

**If the shared pages don't open for non-Claude users:** turn on GitHub Pages for the repo (Settings, then Pages, deploy from the main branch). The pages are plain HTML in `pre-session/` and would then open at a public URL. I haven't tested that, so check it before relying on it. The same HTML is also inside the kit zip, so people who have downloaded the kit can open it offline.

## 7. Promotion

Drafts are in `instructions/promotion/`.

| Post | When | File |
|---|---|---|
| LinkedIn 1: what we're about to do, the scenario, how we're going through a business | Today, Monday | `linkedin-1-today.md` |
| Facebook: for your network, from the everyday person's point of view | Today, Monday (the workshop is tomorrow) | `facebook-post.md` |
| LinkedIn 2: the day-of post | Tomorrow morning | `linkedin-2-tomorrow.md` |

Fill in the Meetup link (already in the drafts) and the kit link after the Release exists.

## 8. Room and day-of

Use `instructions/room-and-recording-checklist.md`. Open items from it that need an answer today:
- [ ] Wi-Fi for 50 devices? Assume it will be slow. Hotspot for you; tell attendees to bring their own connection.
- [ ] Display connection: HDMI or USB-C? Bring both adapters.
- [ ] Microphone for you and a handheld for Q&A.
- [ ] Power strips for attendees.
- [ ] 5:00 setup access, and permission to record.
- [ ] Three helpers named and briefed: two floaters (Starter tier, Builder/Architect tier) and a recorder/timekeeper who calls the clock at 6:28, 6:52 and 7:17.

## 9. Schedule

### Today (Monday, October 5)

| When | Task | Owner |
|---|---|---|
| Now, 30 min | Unzip bundle 4 into the repo, `git rm` the old guide, commit, push. Create the Release. Upload to Drive. | You |
| Next, 20 min | Share both pages. Open them in a private window. Fix what breaks. | You |
| Then, 20 min | Send the Meetup update with real links. Update the event description. | You |
| By early afternoon | Post LinkedIn 1 and the Facebook post. | You |
| In parallel | Draft the speaker script and the 9-slide deck | Claude (say "go") |
| Mid-afternoon, about 2 hours | Full rehearsal on a stopwatch with the Release kit. Log the gotchas. | You |
| After rehearsal | Send me the label and timing differences. I update the pages, plan and kit. | Both |
| Evening, 45 min | Read the script out loud once. Charge everything. Pack. | You |
| Before bed | Confirm helpers, confirm venue answers. | You |

### Tomorrow (Tuesday, October 6)

| When | Task |
|---|---|
| Morning | Post LinkedIn 2. Print `START-HERE.md`. Check your usage allowance. Confirm the Release link still works. |
| Midday | Create "Monday Action Digest" and run it once so a digest already exists. Light check only, to save allowance. |
| 3:30 | Pack: charger, strip, HDMI and USB-C adapters, hotspot, USB sticks, printed pages, mic batteries, water. |
| 5:00 | Venue setup. Test display, mic, hotspot. Start with the QR slide up. |
| 5:30 | Doors. Helpers at the entrance. |
| 6:00 | Welcome: recording notice, pairing, pick a level. |
| 7:30 | Close. Stay for questions. |
| Wednesday | Post the thank-you from `attendee-message.md` section 3. Write the at-home page. |

## 10. Go/no-go at 4:30 PM tomorrow

You're ready if all of these are true:
- [ ] The Release link works from a signed-out browser.
- [ ] Your Cowork opens, on your paid plan, with usage left.
- [ ] A digest is already in `digests/`.
- [ ] You can say the 10 lines without notes.
- [ ] The slides open, and the QR works.
- [ ] You have a hotspot and adapters.
- [ ] Three helpers know their jobs.

**If you only have three hours:** do the Release, the link test, the Meetup update, one run of Parts 1 to 3, and the opening and closing lines. Skip everything else. A smaller, smoother session beats a complete, shaky one.

## 11. Parking lot: not this week

- At-home published page, concepts page and further reading for Session 1 (write on Wednesday).
- Repo license.
- Whether to recreate the public repo so answer keys aren't in the history. (You chose public knowingly. Revisit after Tuesday.)
- Session 2 slides and kit.
- Item 6 of your original Session 1 list, which was never provided.
- The living plan's Month 1 description.
