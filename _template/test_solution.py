import pytest

from .solution import Solution

# Replace with the problem's examples: (args tuple, expected)
CASES = [
    (([1, 2, 3],), 0),
]


@pytest.mark.parametrize(("args", "expected"), CASES)
def test___METHOD__(args, expected):
    assert Solution().__METHOD__(*args) == expected
