# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0

        def maxDepth2(node, height):
            if node == None:
                return height  
            
            return max(maxDepth2(node.left, height + 1), maxDepth2(node.right, height + 1))

        return maxDepth2(root, 0)