import pytest

from .solution import Solution


@pytest.mark.parametrize(
    ("args", "expected"),
    [
        (([1, 2, 3],), 0),
    ],
)
def test_solve(args, expected):
    assert Solution().solve(*args) == expected
