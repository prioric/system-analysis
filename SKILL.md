---
name: system-map
description: "Maps how a company works, from its name and website: ten Markdown chapters of sourced facts, then a first reading in plain words that ends on the decision in front of the company, its options and who pays for each. Use when the user asks to map, read, diagnose or understand a company, its market or its strategy, or says 'run the system map for {company} at {url}'."
license: Apache-2.0
metadata:
  author: prioric
  version: "1.0"
---

# The system map

## Where things are

- `{skill}` is this skill's own folder, the one this file sits in.
- The **working folder** is the folder the agent runs in. `setup.md` and `process.md` sit in it.
- `{company}/` is a folder inside the working folder, one per company, named after the company in lowercase with hyphens. It holds `notes.md`, `chapters/`, `reading.md` and `checks.md`.

`{skill}/examples/` is a finished working folder laid out the same way. Read it before the first run.

## What it makes

1. **The world view.** Ten Markdown chapters in `{company}/chapters/`. Each says how one part of the company works: its market, its buyers, its competitors, what it owns, what it can do, what limits it, how it is run, where its money goes, what it says about itself, and the rules of its trade. Every fact sits in an Evidence bullet that ends on its source and date.
2. **The first reading.** One page, `{company}/reading.md`, in eight parts. It tells what is going on at the company in plain words, shows where the facts pull against each other, and ends on the decision in front of a named body, with the options and the cost of each.

[references/north_star.md](references/north_star.md) describes both outputs and the five rules. Read it whole before anything else.

## The five rules

1. Every figure has a source and a date.
2. Name every actor: the firm, the buyer, the regulator, the body that decides.
3. Describe the company and score nothing. No grades, no stars, no advice.
4. Each finding names who pays: who carries the cost of each pull and each option.
5. A person checks the reading before it reaches anyone outside the run.

## The flow

### 1. Setup, once

When `setup.md` is missing from the working folder, run the interview in [references/setup_interview.md](references/setup_interview.md). Ask one question per message and wait for the answer. Write the answers to `setup.md` from `{skill}/assets/setup_template.md`. When `setup.md` exists, read it and ask nothing.

### 2. Write your own process, once

Read [references/north_star.md](references/north_star.md), [references/chapters.md](references/chapters.md), [references/reading.md](references/reading.md), the example in `{skill}/examples/`, and [references/sample_process.md](references/sample_process.md). Then write `process.md` in the working folder: the steps you will follow to get from a name and a website to a reading that passes the check. Fit it to `setup.md`. A quick run reads less. With no second model there is no second-read step. Without Python you run the checks by reading [references/checks.md](references/checks.md).

Show `process.md` to the person and wait for a yes before the first run. The sample is one way to do it, and yours may differ.

### 3. Run

Follow `process.md`. It always produces these files:

- `{company}/notes.md`: what was read, with dates; the company's own language; the known gaps.
- `{company}/chapters/01_context.md` … `10_sector_rules.md`, in the form of [references/chapters.md](references/chapters.md), from `{skill}/assets/chapter_template.md`.
- `{company}/reading.md`, in the form of [references/reading.md](references/reading.md), from `{skill}/assets/reading_template.md`.

### 4. Check

```
python {skill}/scripts/check_map.py {company}
```

Fix every fault it names and run it again, as often as it takes. Stop only when the same fault is still there after two fixes; then give the person the open faults as a list. Without Python, go through [references/checks.md](references/checks.md) by hand and write the result to `{company}/checks.md`.

### 5. Second read

When `setup.md` names a second model, send it the reading and the chapters with the prompt in [references/second_read.md](references/second_read.md). Fix lists 1, 2, 3, 5 and 6. Give list 4 to the person beside the reading. Run the check again after the fixes. Write one line per check and per read to `{company}/checks.md`.

### 6. Hand over

Give the person `reading.md` and one question: "Is this what is going on at this company?" Beside it, in three lines: the decision and who makes it, what each option costs, and the second reader's strongest left-out explanation.

The reading opens with `Status: draft, not checked by a person`. When the person has checked it, they change the line to `Status: checked by {name} on {date}`, or tell you to. `check_map.py {company} --final` fails while the line still says draft.

### 7. Improve

After each run, ask one question: "What should change in the process next time?" Edit `process.md` and add the date and the change at its foot.

## What the check tests

`scripts/check_map.py` tests the form of the chapters and the reading, and that every number in the reading also sits in a sourced chapter line. It uses Python 3 and its standard library only. It exits 2 on a fault. It cannot tell whether a fact is true, whether a cause is real or whether the right party pays. The second read and the person do that. [references/checks.md](references/checks.md) lists every test.

## What this output is

A draft written by a language model from public sources. Figures can be wrong and causes can be invented. A person checks every figure and every claim against its source before the reading reaches anyone. The authors of this skill take no responsibility for what is made with it.
