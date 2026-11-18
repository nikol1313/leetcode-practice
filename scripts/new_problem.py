#!/usr/bin/env python3
"""Scaffold a new problem from _template/ and add it to the root README table.

Usage: python scripts/new_problem.py 1 "two sum" arrays_hashing easy --lang both
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOPICS = (
    "arrays_hashing",
    "two_pointers",
    "sliding_window",
    "stack",
    "binary_search",
    "linked_list",
    "trees",
    "graphs",
    "dynamic_programming",
    "greedy",
)
DIFFICULTIES = ("easy", "medium", "hard")
LANG_FILES = {
    "py": ("solution.py", "test_solution.py"),
    "js": ("solution.js", "solution.test.js"),
}
TABLE_START, TABLE_END = "<!-- problems:start -->", "<!-- problems:end -->"
STATS_RE = re.compile(r"<!-- stats:start -->.*?<!-- stats:end -->", re.S)


def create_problem(root, number, name, topic, difficulty, langs):
    """Create the problem folder and update README.md. Returns the new folder path."""
    words = re.findall(r"[a-z0-9]+", name.lower())
    if number < 1 or not words:
        raise ValueError("number must be >= 1 and name must contain letters or digits")
    if topic not in TOPICS or difficulty not in DIFFICULTIES:
        raise ValueError(f"unknown topic or difficulty: {topic}, {difficulty}")
    if existing := list((root / "problems").glob(f"*/{number:04d}_*")):
        raise FileExistsError(f"problem {number} already exists: {existing[0]}")

    title = " ".join(w[:1].upper() + w[1:] for w in name.split())
    method = words[0] + "".join(w.capitalize() for w in words[1:])
    if not method.isidentifier():  # e.g. "3sum"
        method = "solve"
    tokens = {
        "{{NUMBER}}": str(number),
        "{{TITLE}}": title,
        "{{SLUG}}": "-".join(words),
        "{{DIFFICULTY}}": difficulty.capitalize(),
        "{{TOPIC}}": topic,
        "__METHOD__": method,
    }

    folder = root / "problems" / topic / f"{number:04d}_{'_'.join(words)}"
    folder.mkdir(parents=True)
    for filename in ("README.md", *(f for lang in langs for f in LANG_FILES[lang])):
        text = (root / "_template" / filename).read_text(encoding="utf-8")
        for token, value in tokens.items():
            text = text.replace(token, value)
        (folder / filename).write_text(text, encoding="utf-8")

    rel = folder.relative_to(root).as_posix()
    py = f"[✅]({rel}/solution.py)" if "py" in langs else ""
    js = f"[✅]({rel}/solution.js)" if "js" in langs else ""
    level = difficulty.capitalize()
    row = f"| {number} | [{title}]({rel}/README.md) | {level} | {topic} | {py} | {js} |"
    _update_readme(root / "README.md", row)
    return folder


def _update_readme(readme, new_row):
    text = readme.read_text(encoding="utf-8")
    head, rest = text.split(TABLE_START)
    body, tail = rest.split(TABLE_END)
    lines = body.strip("\n").splitlines()
    header, rows = lines[:2], lines[2:] + [new_row]
    rows.sort(key=lambda r: int(r.split("|")[1]))

    count = {d: sum(r.split("|")[3].strip().lower() == d for r in rows) for d in DIFFICULTIES}
    stats = (
        "<!-- stats:start -->\n"
        f"**Easy:** {count['easy']} · **Medium:** {count['medium']} · "
        f"**Hard:** {count['hard']} · **Total:** {len(rows)}\n"
        "<!-- stats:end -->"
    )
    table = "\n".join(header + rows)
    text = f"{head}{TABLE_START}\n{table}\n{TABLE_END}{tail}"
    readme.write_text(STATS_RE.sub(stats, text), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("number", type=int)
    parser.add_argument("name")
    parser.add_argument("topic", choices=TOPICS)
    parser.add_argument("difficulty", type=str.lower, choices=DIFFICULTIES)
    parser.add_argument("--lang", choices=("py", "js", "both"), default="both")
    args = parser.parse_args()
    langs = ("py", "js") if args.lang == "both" else (args.lang,)
    try:
        folder = create_problem(ROOT, args.number, args.name, args.topic, args.difficulty, langs)
    except (ValueError, FileExistsError) as e:
        sys.exit(f"error: {e}")
    print(f"created {folder.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
