# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def buildTreeR(preorder_list, inorder_list):
            if not preorder_list or not inorder_list:
                return None
            root = preorder_list[0]
            node = TreeNode(root)
            index = inorder_list.index(root)
            node.left = buildTreeR(preorder_list[1:index+1], inorder_list[:index])
            node.right = buildTreeR(preorder_list[index+1:], inorder_list[index+1:])
            return node 


        return buildTreeR(preorder, inorder)
