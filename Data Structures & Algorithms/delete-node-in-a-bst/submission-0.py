# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def findMin(node):
            if node.left == None:
                return node 

            return findMin(node.left)
            
        def traverse(node):
            if node == None:
                return None

            if key > node.val:
                node.right = traverse(node.right)
                return node

            elif key < node.val:
                node.left = traverse(node.left)
                return node 

            else:
                if node.left == None and node.right == None:
                    return None 
                
                if node.left == None:
                    return node.right

                if node.right == None:
                    return node.left 

                minKey = findMin(node.right)
                node.right = self.deleteNode(node.right, minKey.val)
                minKey.left = node.left 
                minKey.right= node.right
                return minKey 


        return traverse(root)

                
