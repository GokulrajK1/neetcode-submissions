# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invertTree2(root)
        return root

    def invertTree2(self, node):
        if not node:
            return 
        if not node.left and not node.right:
            return 
        
        temp = node.left
        node.left = node.right 
        node.right = temp 
        self.invertTree2(node.left)
        self.invertTree2(node.right)