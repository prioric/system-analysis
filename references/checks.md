# The checks

`scripts/check_map.py` runs every test below and exits 2 on a fault. Without Python, go through this list by hand and write the result to `{company}/checks.md`, one line per test that fails.

## Which check covers which rule

| Rule | The script | The second read | The person |
|---|---|---|---|
| 1. Source and date | every Evidence bullet has one; every number in the reading sits in a sourced chapter line | lists 1 and 3 | checks the figures the decision rests on |
| 2. Name every actor | refuses "the vendor", "the market leader", "the incumbent", "the regulator", "the authorities" or "the client" in a sentence with no name in it | list 5 | reads the names |
| 3. Score nothing | refuses grading words and advice words outside quotes | list 6 | reads the reading |
| 4. Who pays | each pull has a `Who pays:` line; each option has `Cost:` and `carried by` | lists 2 and 6 | judges whether the right party is named |
| 5. A person checks | `--final` refuses a reading still marked draft | none | changes the status line |

The script checks the status line only. It cannot know whether a person really read the page.

## The chapters

1. The ten files are there: `01_context.md`, `02_customers.md`, `03_competition.md`, `04_assets.md`, `05_capabilities.md`, `06_limitations.md`, `07_operating_model.md`, `08_capital_moves.md`, `09_narrative.md`, `10_sector_rules.md`.
2. Each opens on a `# ` title.
3. Each has the five sections `## Summary`, `## Evidence`, `## Confidence`, `## Open questions`, `## Unknowns`. The section headings stay in English in every language, so the check can find them.
4. The Summary has 4 to 6 sentences and gives no advice ("should", "ought to", "recommend").
5. Evidence has 3 bullets or more, and every bullet carries a source in square brackets with a year.
6. Customers has `### The split`. Competition has a table with revenue and margin columns and names the floor. Operating model has `### Who decides`. Capital moves names Invests, Cuts and Hires. Narrative ends on a `Narrative:` and a `Signal:` line. Sector rules has `### Figures that read differently here`.
7. No grading words outside quotes: "out of 5", "world-class", "best-in-class", "strengths", "weaknesses", "SWOT", or "scores high", "rated low" and the like. A buyer that scores bids in a tender is a fact of the trade and passes.

## The reading

1. It opens on a `# ` title sentence.
2. A status line stands in the first lines: `Status: draft, not checked by a person`, or `Status: checked by {name} on {date}`.
3. The parts are numbered `## 1.` to `## 8.`, in order.
4. Parts 1 to 7 each open on a bold sentence.
5. Part 6 has 2 or 3 pulls, each a `### ` heading, each with a `Who pays:` line.
6. Part 7 has 2 to 4 options, each a bullet that opens in bold, each with `Cost:` and `carried by`.
7. No grading words and no advice words outside quotes.
8. No actor from the list in rule 2 stands in a sentence without a name.
9. Every number in the reading also appears in a chapter line that carries a source with a year. Years, and whole numbers below 13, are left out. The number must match exactly: `169,1` matches `169,1`, and `€1.1 billion` matches `€1.1 billion`. The script cannot tell whether the reading uses the number with the same meaning as the chapter; the second read's list 3 checks that.

In another language, the labels `Who pays:`, `Cost:`, `carried by` and the status lines may be the words `setup.md` names for that language.
