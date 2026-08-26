# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        max_sum = float("-inf") 
        
        def dfs(node):

            nonlocal max_sum

            if node == None:
                return 0 

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            print(left, right, node.val)

            curr_max = max(left + node.val, right + node.val)

            max_sum = max(curr_max, max_sum, left + right + node.val)

            return curr_max

        dfs(root)

        return max_sum
