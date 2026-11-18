import shutil
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from new_problem import create_problem  # noqa: E402


@pytest.fixture
def repo(tmp_path):
    shutil.copytree(ROOT / "_template", tmp_path / "_template")
    # Fresh README with an empty table, so these tests don't depend on real progress.
    (tmp_path / "README.md").write_text(
        "<!-- stats:start -->\n<!-- stats:end -->\n"
        "<!-- problems:start -->\n| # | Problem |\n| --- | --- |\n<!-- problems:end -->\n",
        encoding="utf-8",
    )
    (tmp_path / "problems").mkdir()
    return tmp_path


def test_creates_both_languages_and_readme_row(repo):
    folder = create_problem(repo, 1, "two sum", "arrays_hashing", "easy", ("py", "js"))

    assert folder == repo / "problems/arrays_hashing/0001_two_sum"
    assert sorted(p.name for p in folder.iterdir()) == [
        "README.md",
        "solution.js",
        "solution.py",
        "solution.test.js",
        "test_solution.py",
    ]
    assert "def twoSum(self" in (folder / "solution.py").read_text()
    assert "export function twoSum()" in (folder / "solution.js").read_text()
    assert "problems/two-sum/" in (folder / "README.md").read_text()

    readme = (repo / "README.md").read_text()
    assert "| 1 | [Two Sum](problems/arrays_hashing/0001_two_sum/README.md) | Easy |" in readme
    assert "**Easy:** 1 · **Medium:** 0 · **Hard:** 0 · **Total:** 1" in readme


def test_single_language_rows_sorted_and_duplicates_rejected(repo):
    create_problem(repo, 20, "valid parentheses", "stack", "easy", ("js",))
    folder = create_problem(repo, 3, "longest substring", "sliding_window", "medium", ("py",))

    assert not (folder / "solution.js").exists()
    readme = (repo / "README.md").read_text()
    assert readme.index("| 3 |") < readme.index("| 20 |")
    assert "**Easy:** 1 · **Medium:** 1 · **Hard:** 0 · **Total:** 2" in readme
    with pytest.raises(FileExistsError):
        create_problem(repo, 3, "dup", "stack", "easy", ("py",))
