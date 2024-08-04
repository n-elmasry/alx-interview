#!/usr/bin/python3
""" a method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """ a method that determines if all the boxes can be opened."""
    openedboxes = {0}
    keys = list(boxes[0])

    while keys:
        key = keys.pop()
        if key < len(boxes) and key not in openedboxes:
            openedboxes.add(key)
            keys.extend(boxes[key])

    return len(openedboxes) == len(boxes)
