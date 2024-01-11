#!/usr/bin/python3
"""
This module contains a function that checks if all boxes can be unlocked
"""


def canUnlockAll(boxes):
    """ Determines if all boxes can be opened """
    n = len(boxes)
    open_boxes = set([0])
    unopen_boxes = set(boxes[0]).difference(set([0]))
    while len(unopen_boxes) > 0:
        boxIndx = unopen_boxes.pop()
        if not boxIndx or boxIndx >= n or boxIndx < 0:
            continue
        if boxIndx not in open_boxes:
            unopen_boxes = unopen_boxes.union(boxes[boxIndx])
            open_boxes.add(boxIndx)
    return n == len(open_boxes)
