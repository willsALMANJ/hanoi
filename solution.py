"Solution to towers of Hanoi problem"

import argparse
from typing import List, Union

from hanoi import MoveRing, MoveStack, Towers


def other_column(towers, column1, column2):
    "Get other column name"
    return next(c for c in towers.columns if c not in {column1, column2})


def main():
    "Main logic"
    parser = argparse.ArgumentParser()
    parser.add_argument("size", type=int)
    args = parser.parse_args()

    towers = Towers(args.size)

    move_queue: List[Union[MoveRing, MoveStack]] = [
        MoveStack(bottom=towers.size, start="A", end="C")
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
                    other_column(towers, next_move.start, next_move.end),
                ),
                MoveRing(next_move.bottom, next_move.start, next_move.end),
                MoveStack(
                    next_move.bottom - 1,
                    other_column(towers, next_move.start, next_move.end),
                    next_move.end,
                ),
            ]
            move_queue.extend(reversed(new_moves))
        else:
            moves.append(next_move)

    print(f"{towers}")
    for move in moves:
        towers.move(move.start, move.end)
        print(f"{towers}")


if __name__ == "__main__":
    main()
