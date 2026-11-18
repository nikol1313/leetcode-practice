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


def main():
    folders = [p for p in (ROOT / "problems").glob("*/*") if p.is_dir()]
    rows = sorted(problem_row(f) for f in folders)
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
