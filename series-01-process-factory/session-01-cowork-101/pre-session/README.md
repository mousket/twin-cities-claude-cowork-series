# pre-session (attendee-facing, send before Tuesday)

| File | Purpose |
|---|---|
| `01-before-you-come.html` | Pre-meeting check: plan, desktop app, 3-minute practice test, privacy, logistics, troubleshooting, glossary |
| `02-get-the-starter-kit.html` | How to get and unzip the kit from Google Drive or GitHub, and how to confirm the right folder |

Both are single self-contained files (no internet needed once downloaded), work on phones, and follow the reader's light or dark setting.

## Before you share them
1. Open each file in a text editor and find the line `window.COWORK_LINKS = { drive: "", github: "" };`. Paste your Google Drive and GitHub URLs between the quotes in **both** files. Until you do, the buttons say "link to be posted on the Meetup page".
2. In `02-get-the-starter-kit.html`, the GitHub clone command shows `REPO-URL-FROM-THE-GITHUB-PAGE`. Replace it with your repository's clone URL.
3. Rebuild the kit (`python3 scripts/make_kit.py`) so the zip carries the final copies in `before-you-come/`.

## Getting them to attendees before they have the kit
Attendees need these pages before they have the kit, so they can't live only inside the zip. Options: publish them as shareable pages and put the links in the Meetup update, attach the two HTML files to the Meetup message, or enable GitHub Pages on the repository.

## Facts these pages rely on (checked October 2, 2026)
Paid plans only; macOS 11+ or Windows 10+ desktop app; "Cowork" is selected in the message box; Cowork uses more allowance than chat; scheduled tasks are under "Scheduled" in the sidebar. **Not verified:** the exact folder-picker steps and labels, Linux support, how much allowance the session uses.
