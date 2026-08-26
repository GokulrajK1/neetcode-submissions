# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        commonAncestor = [root]

        def isDescendent(node, x):
            if node == None:
                return False

            if node.val == x.val:
                return True

            return isDescendent(node.left, x) or isDescendent(node.right, x)

        def dfs(node):
            if node == None:
                return 
            nonlocal commonAncestor
            x = node == p or isDescendent(node, p)
            y = node == q or isDescendent(node, q)
            print(x, y)
            if x and y:
                print("hi")
                commonAncestor.append(node)
                dfs(node.left)
                dfs(node.right)
            else:
                print("bye")

        dfs(root)
        print([v.val for v in commonAncestor])
        return commonAncestor[-1]


        
            
