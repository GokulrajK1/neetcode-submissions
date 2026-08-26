# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def traverse(node, subRoot):
            if not node:
                return False 

            left = traverse(node.left, subRoot)
            right = traverse(node.right, subRoot)

            return left or right or self.isSameTree(node, subRoot)

        return traverse(root, subRoot)

    def isSameTree(self, node1, node2):
        if not node1 and not node2:
            return True

        if (not node1 and node2) or (node1 and not node2):
            return False 

        return node1.val == node2.val and self.isSameTree(node1.left, node2.left) and self.isSameTree(node1.right, node2.right)