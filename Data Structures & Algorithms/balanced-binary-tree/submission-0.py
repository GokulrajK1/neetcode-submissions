# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if node == None:
                return 0, True

            maxDepthLeft, resLeft = dfs(node.left)
            maxDepthRight, resRight = dfs(node.right)

            if not resLeft or not resRight:
                return 0, False 

            if abs(maxDepthLeft - maxDepthRight) <= 1:
                return 1 + max(maxDepthLeft, maxDepthRight), True
            else:
                return 0, False 

        height, res = dfs(root)
        return res 

