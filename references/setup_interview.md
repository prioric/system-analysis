# The setup interview

Run it once, when `setup.md` is missing from the working folder. Ask one question per message. Wait for the answer before the next question. Keep each question to two lines, and offer the choices. When an answer is unclear, ask once more and then take the default.

Write the answers to `setup.md` from `{skill}/assets/setup_template.md`. Show the finished file to the person in one message. Later runs read it and ask nothing. The person can edit it at any time.

## The six questions

1. **Which AI tool do you use for this?** For example Claude Code, Codex, Gemini CLI, Cursor or another agent. The answer tells you which commands you can run.

2. **Do you pay with an API key or a subscription?** With an API key each run costs money by the token, so a quick run is the default. With a subscription the limit is the plan's usage cap.

3. **Can you reach a second model from another company, and how do you call it?** The second model reads the reading against the chapters before the person does. Two models from one company share blind spots, so another company's model catches more. Offer these choices:
   - `codex exec "{prompt}"` (the Codex command line)
   - `claude -p "{prompt}"` (the Claude Code command line)
   - `gemini -p "{prompt}"` (the Gemini command line)
   - another command the person names
   - none: the second read runs in a fresh session of the same tool, which catches less
   When the person names a command, run it once with the prompt `Reply with the word ready.`, sent the way [second_read.md](second_read.md) sends the pack, and record whether it answered. When it fails, say so in one line and record "none".

4. **Is Python 3 installed?** Do not ask first. Run `python --version`, then `python3 --version`. Ask only when both fail. With Python the check runs as a script. Without it the agent goes through `references/checks.md` by hand.

5. **In which language should the reading be written?** The default is the company's own language: the language of its home-market website and its filings. When the language is not English, write into `setup.md` the words the reading will use for its three labels (`Who pays:`, `Cost:`, `carried by`) and for the status line. Do this yourself, right after the answer, and ask nothing more.

6. **Quick run or deep run?**
   - **Quick:** the company's website, its latest annual report or filing, and one year of news. About an hour of agent time.
   - **Deep:** the website two menu levels deep, five years of filings, the competitors' websites and filings, and two years of news. Several hours.

At the end, ask once: "Do you have writing rules of your own? Paste them or say none." Put them in `setup.md` under "Writing rules".
