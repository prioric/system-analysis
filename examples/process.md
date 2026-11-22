# My process for a system analysis

Written by the agent on 10 November 2026, from the sample process and `setup.md`. Approved by the person on 10 November 2026.

1. Read `setup.md`. Create the company folder and start `notes.md` with the date, the company's language, and where the revenue figures are published.
2. Read the company's website two menu levels deep, its annual reports for the last five years, the boards' published programs and tender notices, the three competitors' annual reports, and two years of trade news. Write each source into `notes.md` with its date. Put pages I cannot reach under "Known gaps".
3. Write the ten chapters, the Evidence first and the Summary last. Put every figure into an Evidence bullet with its source and date.
4. Read only the chapters and list the pulls between pairs of facts in `notes.md`. Keep the two where both sides have filed figures and the most turns on them. Write who carries each one's cost.
5. Write `reading.md` from the chapters and the pulls. Take the body that decides from the "Who decides" list.
6. Run `python scripts/check_map.py alder-pipes`. Fix and run again until it passes.
7. Write the second-read pack and send it with `codex exec --skip-git-repo-check - < alder-pipes/second_read_pack.md`. Fix lists 1, 2, 3, 5 and 6. Run the check again.
8. Give the person `reading.md`, the question, and three lines. Ask what to change next time.

## Changes

- 10 November 2026: the person asked for the tender rules to be read before the chapters, because the guarantee rule changes how every figure reads. Step 2 now reads Westland's general conditions first.
