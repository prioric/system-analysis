# Setup

Written on {date}. The skill reads this file on every run and asks nothing. Edit it at any time.

| Setting | Value |
|---|---|
| AI tool | {the tool the person uses} |
| Paid by | {API key / subscription} |
| Second model | {the command, such as `codex exec "{prompt}"`, or none} |
| Second model answered the test | {yes / no / not tested} |
| Python | {the version, or none} |
| Reading language | {language} |
| Run | {quick / deep} |

## Labels in the reading language

Leave this block out when the reading is in English.

| English | {language} |
|---|---|
| Who pays: | {label} |
| Cost: | {label} |
| carried by | {label} |
| Status: draft, not checked by a person | {line} |
| Status: checked by | {line start} |

## Writing rules

{The person's own rules, one per line, or "none".}
