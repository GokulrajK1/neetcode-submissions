# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        res = root 
        
        def traverse(node, left_bound, right_bound):
            
            nonlocal res 

            if not node: return 

            if node.val > left_bound and node.val > right_bound:
                traverse(node.left, left_bound, right_bound)
            elif node.val < left_bound and node.val < right_bound:
                traverse(node.right, left_bound, right_bound)
            else:
                res = node

        traverse(root, p.val, q.val)

        return res