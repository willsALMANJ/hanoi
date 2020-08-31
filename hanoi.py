"Implementation of Towers class for Towers of Hanoi problem"

from typing import NamedTuple


class MoveRing(NamedTuple):
    "Move a single ring"
    ring: int
    start: str
    end: str


class MoveStack(NamedTuple):
    "Move a stack of rings"
    bottom: int
    start: str
    end: str


class Towers:
    "Towers of Hanoi implementation"

    def __init__(self, size):
        self.size = size
        self.columns = {k: [] for k in "ABC"}
        self.columns["A"] = list(range(size, 0, -1))

    def __str__(self):
        towers = [
            f"{k}: {','.join(str(i) for i in v)}" for k, v in self.columns.items()
        ]
        max_width = len(f"A: {','.join(str(i) for i in range(self.size, 0, -1))}")
        towers = [t.ljust(max_width) for t in towers]
        return "; ".join(towers)

    def __repr__(self):
        return f"{type(self)}({self.size})"

    def move(self, from_col, to_col):
        "Move ring from column to another column"
        ring = self.columns[from_col].pop()
        if self.columns[to_col] and ring > self.columns[to_col][-1]:
            raise RuntimeError(f"Can not move from {from_col} to {to_col}: {self}")
        self.columns[to_col].append(ring)
