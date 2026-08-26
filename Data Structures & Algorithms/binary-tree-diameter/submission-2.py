# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        diameter = 0

        def rDiameterOfBinaryTree(node):
            if node == None:
                return 0

            maxDepthLeft = rDiameterOfBinaryTree(node.left)
            maxDepthRight = rDiameterOfBinaryTree(node.right)
            nonlocal diameter
            diameter = max(diameter, maxDepthLeft + maxDepthRight)

            return 1 + max(maxDepthLeft, maxDepthRight)

        rDiameterOfBinaryTree(root)

        return diameter

        