# pre-session (attendee-facing, send before Tuesday)

| File | Purpose |
|---|---|
| `01-before-you-start.html` | Before You Start: what you need (internet, computer, browser, paid Claude plan, desktop app, VS Code, GitHub or Google account), 3-minute practice test, privacy, session outline, live-meetup logistics, troubleshooting, glossary |
| `02-get-the-starter-kit.html` | How to get and unzip the kit from GitHub Releases or Google Drive, and how to confirm the right folder |

Both are single self-contained files (they only reach out for web fonts, with fallbacks), work on phones, follow the reader's light or dark setting, and remember checklist ticks in the reader's own browser.

## Where they are published
Published copies and their URLs are listed in `PUBLISHED.md` at the repo root. The files here are the source. To update a published page, republish it from the file here; the URL stays the same.

## Settings in the files
Each file has a `window.COWORK_LINKS = { ... }` line near the bottom:
- `github`: the repository URL (set).
- `drive`: the Google Drive link. **Empty for now**; while empty, the Drive card is hidden. Paste the link in both the published page and these files when it exists.
- `kit` and `before`: links between the two pages (relative in these files, full URLs in the published copies).
- The "latest release" button is derived from `github`.

## Before each session
Create the GitHub Release with the zip (`gh release create session-01 birchwood-starter-kit.zip --title "Session 1 starter kit"`), upload the same zip to Drive, then fill in `drive`.

## Facts these pages rely on (checked October 2, 2026)
Paid plans only; macOS 11+ or Windows 10+ desktop app; "Cowork" is selected in the message box; Cowork uses more allowance than chat; scheduled tasks are under "Scheduled" in the sidebar. **Not verified:** the exact folder-picker steps and labels, Linux support, how much allowance the session uses.
