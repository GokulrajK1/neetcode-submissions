# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def traverse(node, max_value):
            if not node: return 0 

            increase = 1 if node.val >= max_value else 0
            return increase + traverse(node.left, max(node.val, max_value)) + traverse(node.right, max(node.val, max_value))

        return traverse(root, float('-inf'))
