#!/usr/bin/env python3
"""Check a system analysis: the ten chapters and the first reading of one company.

    python check_map.py {company}            check {company}/chapters/, and {company}/reading.md when it exists
    python check_map.py {company} --final    also refuse a reading whose status line still says draft
    python check_map.py {company} --chapters-only

The reading is optional. When setup.md has the row '| First reading | yes |', a missing reading.md is a fault.

The labels of a reading in another language are read from setup.md in the folder above {company}
(or the file given with --setup). Python 3 and its standard library only.
Prints one line per fault and exits 2 when there is any. Exit 0 is clean.
"""
import argparse
import re
import sys
from pathlib import Path

NAMES = ["01_context", "02_customers", "03_competition", "04_assets", "05_capabilities",
         "06_limitations", "07_operating_model", "08_capital_moves", "09_narrative", "10_sector_rules"]
SECTIONS = ["Summary", "Evidence", "Confidence", "Open questions", "Unknowns"]

# A buyer that scores bids in a tender is a fact of the trade, so a bare "score" passes. These words
# mark the writer grading the company.
SCORE = re.compile(r"\b(out of (?:5|10)|world[- ]class|best[- ]in[- ]class|strengths|weaknesses|SWOT|"
                   r"(?:scores?|scored|rated|grades?|graded) (?:high|low|well|poorly|badly|strongly|weakly))\b",
                   re.I)
ADVICE = re.compile(r"\b(should|ought to|recommend(?:s|ed|ation)?|we suggest|it is advisable)\b", re.I)
VAGUE = re.compile(r"\bthe (vendor|market leader|incumbent|regulator|authorities|client)\b", re.I)
SOURCE = re.compile(r"\[[^\]]*\b(?:19|20)\d\d\b[^\]]*\]")
NUMBER = re.compile(r"(?<![\w.,])\d+(?:[.,]\d+)*")
YEAR = re.compile(r"^(?:19|20)\d\d$")

DEFAULT_LABELS = {
    "who_pays": "Who pays:",
    "cost": "Cost:",
    "carried_by": "carried by",
    "status_draft": "Status: draft, not checked by a person",
    "status_checked": "Status: checked by",
}
LABEL_ROWS = {
    "Who pays:": "who_pays",
    "Cost:": "cost",
    "carried by": "carried_by",
    "Status: draft, not checked by a person": "status_draft",
    "Status: checked by": "status_checked",
}


def section(text, name):
    """The body of the '## {name}' section, or None when there is no such heading."""
    m = re.search(r"^##\s+" + re.escape(name) + r"\s*$(.*?)(?=^##\s|\Z)", text, re.M | re.S)
    return m.group(1).strip() if m else None


def sentences(text):
    text = re.sub(r"\s+", " ", text.strip())
    return [s for s in re.split(r"(?<=[.!?])\s+(?=[A-ZÀ-ɏ\"“(])", text) if s.strip()]


def sourced_lines(text):
    return [l for l in text.splitlines() if SOURCE.search(l)]


def numbers(text):
    return set(NUMBER.findall(text))


def check_chapters(folder):
    faults, bank = [], set()
    folder = Path(folder)
    if not folder.is_dir():
        return [f"no chapters folder at {folder}"], bank
    for name in NAMES:
        hits = sorted(folder.glob(name + "*.md"))
        if not hits:
            faults.append(f"missing chapter: {name}.md")
            continue
        path = hits[0]
        tag = path.name
        text = path.read_text(encoding="utf-8")
        for line in sourced_lines(text):
            bank |= numbers(line)
        if not re.match(r"#\s+\S", text.lstrip()):
            faults.append(f"{tag}: the file opens on a '# ' title")
        for h in SECTIONS:
            if section(text, h) is None:
                faults.append(f"{tag}: missing section '## {h}'")
        summary = section(text, "Summary") or ""
        n = len(sentences(summary))
        if summary and not 4 <= n <= 6:
            faults.append(f"{tag}: the Summary has {n} sentences; it takes 4 to 6")
        for m in ADVICE.finditer(summary):
            faults.append(f"{tag}: advice in the Summary: '{m.group(0)}'")
        evidence = section(text, "Evidence") or ""
        bullets = [b.strip() for b in evidence.splitlines() if re.match(r"\s*[-*]\s", b)]
        if evidence and len(bullets) < 3:
            faults.append(f"{tag}: Evidence has {len(bullets)} bullets; it takes 3 or more")
        for b in bullets:
            if not SOURCE.search(b):
                faults.append(f"{tag}: an Evidence bullet ends on no [source, year]: {b[:80]}")
        body = re.sub(r"\[[^\]]*\]", "", text)
        body = re.sub(r"\"[^\"]*\"|“[^”]*”", "", body)
        for m in SCORE.finditer(body):
            faults.append(f"{tag}: a scoring word outside a quote: '{m.group(0)}'")
        if name == "02_customers" and not re.search(r"^###\s+The split", text, re.M):
            faults.append(f"{tag}: no '### The split' table of the buyer groups")
        if name == "03_competition":
            rows = [l for l in text.splitlines() if l.strip().startswith("|")]
            if not any(re.search(r"revenue", r, re.I) and re.search(r"margin", r, re.I) for r in rows):
                faults.append(f"{tag}: no peer table with revenue and margin columns")
            if not re.search(r"\bfloor\b", text, re.I):
                faults.append(f"{tag}: the floor (the buyer doing nothing) is not named")
        if name == "07_operating_model" and not re.search(r"^###\s+Who decides", text, re.M):
            faults.append(f"{tag}: no '### Who decides' list")
        if name == "08_capital_moves":
            for part in ("Invests", "Cuts", "Hires"):
                if not re.search(r"\b" + part + r"\b", text):
                    faults.append(f"{tag}: the part '{part}' is missing")
        if name == "09_narrative":
            for line in ("Narrative:", "Signal:"):
                if not re.search(r"^\**" + line + r"\**\s*\S", text, re.M):
                    faults.append(f"{tag}: no closing line '{line} …'")
        if name == "10_sector_rules" and not re.search(r"^###\s+Figures that read differently here", text, re.M):
            faults.append(f"{tag}: no '### Figures that read differently here' list")
    return faults, bank


def read_labels(setup):
    labels = dict(DEFAULT_LABELS)
    alt = {}
    if setup and Path(setup).is_file():
        for line in Path(setup).read_text(encoding="utf-8").splitlines():
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) == 2 and cells[0] in LABEL_ROWS and cells[1] and not cells[1].startswith("{"):
                alt[LABEL_ROWS[cells[0]]] = cells[1]
    return labels, alt


def reading_wanted(setup):
    """True when setup.md has the row '| First reading | yes |'."""
    if not setup or not Path(setup).is_file():
        return False
    for line in Path(setup).read_text(encoding="utf-8").splitlines():
        cells = [c.strip().lower() for c in line.strip().strip("|").split("|")]
        if len(cells) == 2 and cells[0] == "first reading":
            return cells[1].startswith("yes")
    return False


def has_label(text, key, labels, alt, start=False):
    for lab in (labels[key], alt.get(key)):
        if not lab:
            continue
        if start and text.lstrip("*").strip().lower().startswith(lab.lower()):
            return True
        if not start and lab.lower() in text.lower():
            return True
    return False


def parts(text):
    """The '## N.' parts in the order they stand: a list of (number, heading, body)."""
    out = []
    for m in re.finditer(r"^##\s+(\d+)\.\s*(.*?)\s*$(.*?)(?=^##\s|\Z)", text, re.M | re.S):
        out.append((int(m.group(1)), m.group(2), m.group(3).strip()))
    return out


def check_reading(path, bank, labels, alt, final):
    faults = []
    path = Path(path)
    if not path.is_file():
        return [f"no reading at {path}"]
    text = path.read_text(encoding="utf-8")
    head = text.splitlines()[:12]
    if not text.lstrip().startswith("# "):
        faults.append("reading.md: the page opens on a '# ' title sentence")
    status = [l for l in head if has_label(l, "status_draft", labels, alt, start=True)
              or has_label(l, "status_checked", labels, alt, start=True)]
    if not status:
        faults.append("reading.md: no status line in the first lines ('Status: draft, not checked by a person')")
    elif final and not has_label(status[0], "status_checked", labels, alt, start=True):
        faults.append("reading.md: the status line still says draft; a person checks the reading first")
    found = parts(text)
    nums = [n for n, _, _ in found]
    if nums != list(range(1, 9)):
        faults.append(f"reading.md: the parts are numbered {nums}; they run '## 1.' to '## 8.' in order")
    byn = {n: (h, b) for n, h, b in found}
    for n in range(1, 8):
        if n not in byn:
            continue
        body = byn[n][1]
        first = next((l for l in body.splitlines() if l.strip()), "")
        if not first.strip().startswith("**"):
            faults.append(f"reading.md: part {n} opens on no bold sentence that states what it finds")
    if 6 in byn:
        pulls = re.split(r"^###\s+", byn[6][1], flags=re.M)[1:]
        if not 2 <= len(pulls) <= 3:
            faults.append(f"reading.md: part 6 has {len(pulls)} pulls ('### ' headings); it takes 2 or 3")
        for p in pulls:
            title = p.splitlines()[0].strip()
            if not any(has_label(l, "who_pays", labels, alt, start=True) for l in p.splitlines()):
                faults.append(f"reading.md: the pull '{title}' has no 'Who pays:' line")
    if 7 in byn:
        options = [l for l in byn[7][1].splitlines() if re.match(r"\s*[-*]\s+\*\*", l)]
        if not 2 <= len(options) <= 4:
            faults.append(f"reading.md: part 7 has {len(options)} options ('- **…**' bullets); it takes 2 to 4")
        for o in options:
            if not has_label(o, "cost", labels, alt):
                faults.append(f"reading.md: an option has no 'Cost:': {o.strip()[:70]}")
            if not has_label(o, "carried_by", labels, alt):
                faults.append(f"reading.md: an option names no one it is 'carried by': {o.strip()[:70]}")
    body = re.sub(r"\"[^\"]*\"|“[^”]*”", "", text)
    for m in SCORE.finditer(body):
        faults.append(f"reading.md: a scoring word outside a quote: '{m.group(0)}'")
    for m in ADVICE.finditer(body):
        faults.append(f"reading.md: an advice word outside a quote: '{m.group(0)}'")
    for s in sentences(re.sub(r"^#.*$", "", body, flags=re.M)):
        m = VAGUE.search(s)
        if m and not re.search(r"(?<!^)\b[A-Z][a-z]+", s[1:]):
            faults.append(f"reading.md: an actor with no name: '{m.group(0)}' in: {s[:70]}")
    counted = "\n".join(l for l in text.splitlines()
                        if not re.match(r"\s*(#|Status:|Evidence current as of)", l)
                        and not any(has_label(l, k, labels, alt, start=True) for k in ("status_draft", "status_checked")))
    for tok in sorted(numbers(counted)):
        plain = tok.replace(",", "").replace(".", "")
        if YEAR.match(tok) or (plain.isdigit() and "," not in tok and "." not in tok and int(plain) < 13):
            continue
        if tok not in bank:
            faults.append(f"reading.md: the figure '{tok}' sits in no chapter line that carries a [source, year]")
    return faults


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("company", help="the company folder, holding chapters/ and reading.md")
    ap.add_argument("--final", action="store_true", help="refuse a reading still marked draft")
    ap.add_argument("--chapters-only", action="store_true", help="check the chapters and skip the reading")
    ap.add_argument("--setup", help="setup.md with the labels of the reading language")
    a = ap.parse_args()
    company = Path(a.company)
    faults, bank = check_chapters(company / "chapters")
    setup = Path(a.setup) if a.setup else company.resolve().parent / "setup.md"
    wants_reading = reading_wanted(setup)
    has_reading = (company / "reading.md").is_file()
    if wants_reading and not has_reading and not a.chapters_only:
        faults.append("setup.md asks for the first reading, and there is no reading.md")
    check_it = has_reading and not a.chapters_only
    if check_it:
        labels, alt = read_labels(setup)
        faults += check_reading(company / "reading.md", bank, labels, alt, a.final)
    for f in faults:
        print(f"FAIL  {f}")
    if faults:
        print(f"{len(faults)} fault(s)")
        sys.exit(2)
    print("OK  the chapters" + (" and the reading" if check_it else "") + " pass")


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    main()
