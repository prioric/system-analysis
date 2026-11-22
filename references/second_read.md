# The second read

A second model reads the reading against the chapters before the person does. `setup.md` names it. Two models from one company share blind spots, so the reader is picked in this order:

1. **Another company's model**, called by the command in `setup.md`. This read catches the most.
2. **The same tool in a fresh session** that has not seen the writing, when `setup.md` says none. It catches less.

The person is told which kind of read ran: "second read by another company's model", "second read in a fresh session of the same tool", or "no second read".

## How to call it

The model gets one prompt with three parts: the prompt below with the company filled in, the reading, and the ten chapters. Write them into one file, `{company}/second_read_pack.md`, and pass the file. Long text on a command line breaks on some systems.

| Command in `setup.md` | How to send the pack |
|---|---|
| `codex exec` | `codex exec --skip-git-repo-check - < {company}/second_read_pack.md` |
| `claude -p` | `claude -p < {company}/second_read_pack.md` |
| `gemini -p` | `gemini --skip-trust -p "Follow the instructions in the text on standard input." < {company}/second_read_pack.md` |

Codex refuses to run outside a git folder unless it gets `--skip-git-repo-check`. Gemini refuses a folder it has not been told to trust unless it gets `--skip-trust`.
| another command | the way the person described in the interview |

Save the answer to `{company}/second_read.md`.

## The prompt

```
You read a first reading of {company}. After it come the ten chapters it was cut from. Read the
reading against the chapters and return six lists. Quote the sentence you mean in each item.
Return nothing else.

1. Claims no chapter supports: a sentence with a fact, a figure or a name that is in no chapter.
2. Cause-and-effect sentences the chapters do not back: a sentence that says one thing happened
   because of another, where the chapters show both things and no link.
3. Figures bound to the wrong firm, unit, year or scope.
4. The strongest explanation the reading left out: one paragraph on the reading of the same
   chapters that explains the facts as well or better. Where the reading's own explanation is
   the strongest, say so in one line.
5. Sentences a stranger must read twice, each with a plain rewrite. Include any actor written
   without a name, such as "the regulator" or "the vendor".
6. Any sentence that scores the company, gives advice, or names no one who carries a cost.

Judge nothing about the company. Judge the reading against the chapters.
```

## What to do with the answer

- Lists 1, 2 and 3: fix the sentence. When the chapter is wrong, fix the chapter first, then the reading.
- List 4: do not rewrite the reading on the second reader's word. Give the paragraph to the person beside the reading, because the person decides between two readings.
- Lists 5 and 6: put the rewrites into the reading.
- Run the check again after the fixes.
- Write one line to `{company}/checks.md`: the date, the command, the kind of read, and how many items each list had.

One read and one fix pass. The output then goes to the person with any open points listed.
