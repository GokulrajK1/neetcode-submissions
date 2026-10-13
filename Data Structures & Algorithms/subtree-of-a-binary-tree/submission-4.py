# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverse(node1, node2):
            if (node1 is None) != (node2 is None):
                return False 

            if not node1 and not node2:
                return True 

            return node1.val == node2.val and traverse(node1.left, node2.left) and traverse(node1.right, node2.right)

        return traverse(p, q)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot: return True 
        if not root and subRoot: return False 
        
        def traverse(node):
            if not node: return False 
            return traverse(node.left) or traverse(node.right) or self.isSameTree(node, subRoot)

        return traverse(root)