# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def get_minimum_node(node):
            if not node: return None
            if not node.left: return node 
            return get_minimum_node(node.left)

        def delete(node, key):
            if not node: return
            if key < node.val: node.left = delete(node.left, key)
            elif key > node.val: node.right = delete(node.right, key)
            else:
                if not node.left: return node.right
                if not node.right: return node.left

                temp = get_minimum_node(node.right)
                node.right = delete(node.right, temp.val)
                temp.left = node.left
                temp.right = node.right
                node = temp

            return node 

        return delete(root, key)

    

         


        