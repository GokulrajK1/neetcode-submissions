# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        indicies = {}
        for i, value in enumerate(inorder):
            indicies[value] = i 

        pre_order_index = 0

        def traverse(left, right):
            nonlocal pre_order_index
            
            if left > right: return None 
            value = preorder[pre_order_index]
            pre_order_index += 1
            index = indicies[value]
            root = TreeNode(value)
            root.left = traverse(left, index - 1)
            root.right = traverse(index + 1, right)
            return root 

        return traverse(0, len(preorder) - 1)
        