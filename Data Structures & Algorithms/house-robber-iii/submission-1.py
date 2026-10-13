# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def traverse(node):
            if not node: return (0, 0)

            with_left, without_left = traverse(node.left)
            with_right, without_right = traverse(node.right)

            return (node.val + without_left + without_right, max(with_left, without_left) + max(without_right, with_right))

        return max(traverse(root))