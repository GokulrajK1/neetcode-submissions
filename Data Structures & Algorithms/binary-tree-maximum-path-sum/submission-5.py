# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        max_sum = float("-inf")

        def traverse(node):
            
            nonlocal max_sum

            if not node: return 0

            left = traverse(node.left)
            right = traverse(node.right)

            max_sum = max(max_sum, node.val, node.val + left, node.val + right, node.val + left + right)

            return max(node.val, node.val + left, node.val + right)

        traverse(root)

        return max_sum