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

            if node.val > p.val and node.val > q.val:
                traverse(node.left)

            elif node.val < p.val and node.val < q.val:
                traverse(node.right)

            else:
                res = node
                return 

        


        traverse(root)

        return res

            