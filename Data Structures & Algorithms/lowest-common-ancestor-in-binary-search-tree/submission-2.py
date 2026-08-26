# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        res = None

        def dfs(node):

            nonlocal res

            if node == None:
                return None
            
            if node.val > p.val and node.val > q.val:
                print("left")
                res = node 
                dfs(node.left)

            elif node.val < p.val and node.val < q.val:
                print("right")
                res = node 
                dfs(node.right)

            else:
                print("found")
                res = node
                return 

        dfs(root)
        return res