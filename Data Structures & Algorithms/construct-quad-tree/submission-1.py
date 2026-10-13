"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def traverse(i, j, n):
            if n == 1:
                return Node(True if grid[i][j] else False, isLeaf=True)

            topLeft = traverse(i, j, n // 2)
            topRight = traverse(i, j + n // 2, n // 2)
            bottomLeft = traverse(i + n // 2, j, n // 2)
            bottomRight = traverse(i + n // 2, j + n // 2, n // 2)

            if not topLeft.isLeaf or not topRight.isLeaf or not bottomLeft.isLeaf or not bottomRight.isLeaf:
                return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)

            if topLeft.val and topRight.val and bottomLeft.val and bottomRight.val:
                return Node(True, isLeaf=True)

            if not topLeft.val and not topRight.val and not bottomLeft.val and not bottomRight.val:
                return Node(False, isLeaf=True)

            return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)

        return traverse(0, 0, len(grid))

            