#!/usr/bin/python3
"""Module for determining whether all lockboxes can be unlocked."""


def canUnlockAll(boxes):
    """Return True if all boxes can be unlocked, otherwise False."""
    unlocked = {0}
    to_visit = [0]

    while to_visit:
        box = to_visit.pop()

        for key in boxes[box]:
            if 0 <= key < len(boxes) and key not in unlocked:
                unlocked.add(key)
                to_visit.append(key)

    return len(unlocked) == len(boxes)
