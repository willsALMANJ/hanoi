"Solution to towers of Hanoi problem"

import argparse
from typing import List, NamedTuple, Union

from hanoi import Towers


class MoveRing(NamedTuple):
    "Move a single ring"
    ring: int
    start: str
    end: str


class MoveStack(NamedTuple):
    "Move a stack of rings starting at bottom up to 1"
    bottom: int
    start: str
    end: str


def _other_column(columns: List[str], column1: str, column2: str) -> str:
    "Helper function to get third column's name"
    return next(c for c in columns if c not in {column1, column2})


def solve(size: int, columns: List[str]) -> List[MoveRing]:
    """Generate a list of moves that solve the Towers of Hanoi problem

    Args:
        size: the number of rings in the game
        columns: list of labels to use for the columns. The first list entry
            should be the column on which all the rings starts. The last entry
            should be the column where all the rings should be moved.

    Returns:
        the list of moves
    """
    move_queue: List[Union[MoveRing, MoveStack]] = [
        MoveStack(bottom=size, start=columns[0], end=columns[-1])
    ]
    moves: List[MoveRing] = []

    while move_queue:
        next_move = move_queue.pop()
        if isinstance(next_move, MoveStack) and next_move.bottom == 1:
            move_queue.append(MoveRing(1, next_move.start, next_move.end))
        elif isinstance(next_move, MoveStack):
            new_moves = [
                MoveStack(
                    next_move.bottom - 1,
                    next_move.start,
                    _other_column(columns, next_move.start, next_move.end),
                ),
                MoveRing(next_move.bottom, next_move.start, next_move.end),
                MoveStack(
                    next_move.bottom - 1,
                    _other_column(columns, next_move.start, next_move.end),
                    next_move.end,
                ),
            ]
            move_queue.extend(reversed(new_moves))
        else:
            moves.append(next_move)

    return moves


def main():
    "Main logic"
    parser = argparse.ArgumentParser("Print a solution to the Towers of Hanoi problem.")
    parser.add_argument("size", type=int)
    args = parser.parse_args()

    towers = Towers(args.size)
    moves = solve(args.size, list(towers.columns))

    print(f"{towers}")
    for move in moves:
        towers.move(move.start, move.end)
        print(f"{towers}")


if __name__ == "__main__":
    main()
