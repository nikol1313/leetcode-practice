"""Rebuild the progress section of README.md from the folders in problems/."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
START, END = "<!-- progress:start -->", "<!-- progress:end -->"
LEVELS = ("Easy", "Medium", "Hard")


def problem_row(folder):
    readme = folder / "README.md"
    text = readme.read_text(encoding="utf-8") if readme.exists() else ""

    number = re.match(r"\d*", folder.name).group().lstrip("0")
    heading = re.search(r"^#\s+(?:\d+\.\s*)?(.+)$", text, re.M)
    title = heading.group(1).strip() if heading else ""
    if not title or title == "Problem Name":  # untouched template heading
        title = re.sub(r"^\d+_?", "", folder.name).replace("_", " ").title()

    level = re.search(r"\*\*Difficulty:\*\*[ \t]*(\w+)[ \t]*$", text, re.M)
    level = level.group(1).capitalize() if level else ""
    level = level if level in LEVELS else "?"

    rel = folder.relative_to(ROOT).as_posix()
    link = f"[{title}]({rel}/README.md)" if readme.exists() else f"[{title}]({rel})"

    def lang(ext):
        files = sorted(folder.glob(f"*.{ext}"))
        return f"[✅]({rel}/{files[0].name})" if files else ""

    return (int(number or 0), folder.name), level, (
        f"| {number} | {link} | {level} | {folder.parent.name} | {lang('py')} | {lang('js')} |"
    )


def file_row(stem, files):
    """One problem saved as loose files, e.g. problems/two_pointers/455.py (+ 455.js)."""
    text = "\n".join(f.read_text(encoding="utf-8") for f in files)
    topic = files[0].parent.name
    number = re.match(r"\d*", stem).group().lstrip("0")

    # header comments: "# problem: assign cookies" / "// Two Sum", then "# Difficulty: Easy"
    heading = re.search(r"^\s*(?:#|//)\s*(?:problem:\s*)?(.+?)\s*$", text, re.M | re.I)
    title = heading.group(1) if heading else stem
    title = title.title() if title.islower() else title

    level = re.search(r"^\s*(?:#|//)\s*Difficulty:\s*(\w+)", text, re.M | re.I)
    level = level.group(1).capitalize() if level else ""
    level = level if level in LEVELS else "?"

    rel = files[0].parent.relative_to(ROOT).as_posix()
    by_ext = {f.suffix: f.name for f in files}
    link = f"[{title}]({rel}/{files[0].name})"

    def lang(ext):
        return f"[✅]({rel}/{by_ext[ext]})" if ext in by_ext else ""

    return (int(number or 0), stem), level, (
        f"| {number} | {link} | {level} | {topic} | {lang('.py')} | {lang('.js')} |"
    )


def main():
    folders = [p for p in (ROOT / "problems").glob("*/*") if p.is_dir()]
    rows = [problem_row(f) for f in folders]

    loose = {}
    for f in (ROOT / "problems").glob("*/*"):
        if f.is_file() and f.suffix in (".py", ".js") and f.stat().st_size:  # skip empty stubs
            loose.setdefault((f.parent, f.stem), []).append(f)
    rows += [file_row(stem, sorted(fs)) for (_, stem), fs in loose.items()]
    rows.sort()
    counts = {lv: sum(level == lv for _, level, _ in rows) for lv in LEVELS}
    section = "\n".join(
        [
            START,
            f"**Easy:** {counts['Easy']} · **Medium:** {counts['Medium']} · "
            f"**Hard:** {counts['Hard']} · **Total:** {len(rows)}",
            "",
            "| # | Problem | Difficulty | Topic | Python | JavaScript |",
            "| --- | --- | --- | --- | --- | --- |",
            *(row for _, _, row in rows),
            END,
        ]
    )
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    before, rest = text.split(START)
    after = rest.split(END)[1]
    path.write_text(before + section + after, encoding="utf-8")


if __name__ == "__main__":
    main()
