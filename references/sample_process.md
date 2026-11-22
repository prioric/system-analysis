# A sample process

This is one way to get from a name and a website to a reading that passes the check. Write your own `process.md` from it, fitted to `setup.md`. Keep what works and change the rest.

## 0. Set up

Read `setup.md`. Create `{company}/`. Start `{company}/notes.md` with the date, the company's own language (the language of its home-market website and filings), and whether it publishes revenue and profit figures, and where you looked.

## 1. Read the evidence

Read the company's website: every page its menus list, one level deep on a quick run and two levels on a deep run. Read its latest annual report or filing; on a deep run, five years of them. Read the news: one year on a quick run, two on a deep run. On a deep run, also read the websites and filings of the competitors the company names and the competitors the trade press names.

Write what you read into `notes.md` as a list with dates. A page that cannot be reached goes under "Known gaps". End the notes with up to four topics to look at first. The notes set the focus. They never set the conclusion.

## 2. Write the ten chapters

Write the ten chapters from the evidence alone, in the form of `{skill}/references/chapters.md`. Write the facts first and the Summary last, because the Summary only restates the Evidence.

## 3. Find the pulls

Read the ten chapters and nothing else. Hold pairs of facts against each other:

- what the company says it will do, against what it is seen doing;
- what the market asks for, against what the company has;
- where the market is going, against where the money is going;
- a limit, against a move;
- one capital move, against another.

Keep a pull when the head of the company would say "yes, that is our problem", when a competitor's name in its place makes the sentence false, and when no rule in the Sector rules chapter explains it away. Keep two or three, the ones where both sides are well sourced and the most turns on them. For each, write who carries its cost and by when. Keep this list in `notes.md`.

## 4. Write the reading, when `setup.md` asks for it

Cut the reading from the chapters and the pulls, in the form of `{skill}/references/reading.md`. Part 7 needs the body that decides, from the "Who decides" list in the Operating model chapter, and two to four options with what each costs and who carries it.

## 5. Check

Run `python {skill}/scripts/check_map.py {company}`, or go through `{skill}/references/checks.md` by hand. Fix and run again until it passes.

## 6. Second read

Send the reading and the chapters to the second model in `setup.md`, with the prompt in `{skill}/references/second_read.md`. Fix, then check again.

## 7. Hand over

Give the person `reading.md`, the question "Is this what is going on at this company?", and three lines: the decision and who makes it, what each option costs, and the second reader's strongest left-out explanation. Then ask what should change in the process next time.
