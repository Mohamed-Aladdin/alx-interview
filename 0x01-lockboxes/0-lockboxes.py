#!/usr/bin/python3
'''A module for lockboxes.
'''


def canUnlockAll(boxes):
    '''You have n number of locked boxes in front of you.
    Each box is numbered sequentially from 0 to n - 1
    and each box may contain keys to the other boxes.
    A method that determines if all the boxes can be opened.
    '''
    n = len(boxes)
    vis_boxes = set([0])
    invis_boxes = set(boxes[0]).difference(set([0]))

    while len(invis_boxes) > 0:
        boxIdx = invis_boxes.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in vis_boxes:
            invis_boxes = invis_boxes.union(boxes[boxIdx])
            vis_boxes.add(boxIdx)
    return n == len(vis_boxes)
