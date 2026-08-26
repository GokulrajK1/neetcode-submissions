# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        res = None

        def traverse(node):
            nonlocal res

            if not node:
                return 

            if (node.val >= p.val and node.val <= q.val) or (node.val <= p.val and node.val >= q.val):
                res = node
                return 

            if node.val > p.val and node.val > q.val:
                print('left')
                traverse(node.left)

            else:
                print('right')
                traverse(node.right)


        traverse(root)

        return res

            