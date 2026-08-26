"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def recurse(grid, n, r, c):

            if n == 1:
                print("n=1", r, c, f"val={grid[r][c]}")
                return Node(grid[r][c], True, None, None, None, None) 

            topleft = recurse(grid, n // 2, r, c)
            bottomleft = recurse(grid, n // 2, r + n // 2, c)
            topright = recurse(grid, n // 2, r, c + n // 2)
            bottomright = recurse(grid, n // 2, r + n // 2, c + n // 2)

            print(f'n={n}', r, c)

            if (topleft.isLeaf and topright.isLeaf and bottomleft.isLeaf and bottomright.isLeaf) and (topleft.val == topright.val == bottomleft.val == bottomright.val):
                print("leaf found", topleft.val)
                return Node(topleft.val, True, None, None, None, None)
            else:
                print("not leaf", topleft.val, topright.val, bottomleft.val, bottomright.val)
                return Node(topleft.val, False, topleft, topright, bottomleft, bottomright)

        return recurse(grid, len(grid), 0, 0)
            

        