# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0 

        def dfs(node, val):

            nonlocal res

            if node == None:
                return None

            if node.val >= val:
                res += 1 

            dfs(node.left, max(val, node.val))
            dfs(node.right, max(val, node.val))

        dfs(root, -1000)

        return res
            
            

        