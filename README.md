# System analysis

An AI agent skill that maps how a company works, from its name and its website. It makes the world view other skills draw from, and on request a one-page reading:

1. **The world view:** ten chapters of facts about the company. They cover its market, buyers, competitors, assets, capabilities, limits, how it is run, where its money goes, what it says about itself, and the rules of its trade. Every fact carries its source and date.
2. **The first reading, optional:** one page in eight parts. It says what is going on at the company in plain words and where the facts pull against each other. It ends on the decision in front of a named body, with each option's cost and who carries it.

The skill describes the company and scores nothing. It gives no advice.

The skill follows the open [Agent Skills](https://agentskills.io) format: a `SKILL.md` with the instructions, reference files the agent reads, and one Python script the agent runs to check its own work. The script uses Python 3 and its standard library only. Without Python, the agent runs the same checks from a written list.

## Install

Copy this folder into the folder your agent reads skills from, under the name `prioric-system-analysis`. For Claude Code:

```
git clone https://github.com/prioric/system-analysis.git ~/.claude/skills/prioric-system-analysis
```

For another agent, copy the folder where that agent finds its skills, or point the agent at `SKILL.md`.

## First run

Ask your agent: "Run the system analysis for {company} at {website}."

On the first run the agent asks seven short questions, one at a time:

1. Which AI tool do you use?
2. Do you pay with an API key or a subscription?
3. Can you reach a second model from another company, and with which command? For example `codex exec`, `claude -p` or `gemini -p`. The second model checks the work before you read it. Two companies' models miss different things.
4. Is Python installed? The agent tests this itself first.
5. In which language should the reading be written?
6. Quick run or deep run?
7. Do you also want the first reading? The default is no.

It writes your answers to `setup.md` in your working folder, so later runs ask nothing. Then it writes its own `process.md`, the steps it will follow, and shows it to you. It starts after your yes. After each run it asks what to change and edits `process.md`.

## What you get

```
setup.md                 your answers, once
process.md               the agent's own steps, which you approve
{company}/
  notes.md               what was read, with dates, and the known gaps
  chapters/              the ten chapters
  reading.md             the first reading, when asked for
  checks.md              one line per check and per second read
```

## What is here

| Path | What is in it |
|---|---|
| `SKILL.md` | The instructions the agent follows. |
| `references/north_star.md` | The two outputs, the five rules, and how to write. |
| `references/setup_interview.md` | The seven questions. |
| `references/chapters.md` | The ten chapters and their form. |
| `references/reading.md` | The eight parts of the reading. |
| `references/second_read.md` | The prompt for the second model, and how to call it. |
| `references/sample_process.md` | One sample process the agent writes its own from. |
| `references/checks.md` | Every check, in words, for a run without Python. |
| `scripts/check_map.py` | Checks the chapters and the reading. Exits 2 on a fault. |
| `assets/` | The templates for `setup.md`, a chapter and the reading. |
| `examples/` | A finished working folder for Alder Pipes, an invented pipeline builder: the setup, the process, the notes, the ten chapters and the reading. |

To see the check pass on the example:

```
python scripts/check_map.py examples/alder-pipes
```

## What this output is

A draft written by a language model from public sources. Figures can be wrong and causes can be invented. A person checks every figure and every claim against its source before the reading reaches anyone. The reading's first line records that check. The authors take no responsibility for what is made with it.

## License

Apache License 2.0. See `LICENSE`.
