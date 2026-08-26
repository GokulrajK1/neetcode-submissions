# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        count = 0
        queue = deque([[root, root.val]])
        while queue:
            for i in range(len(queue)):
                node, max_val = queue.popleft()
                if node.val >= max_val:
                    count +=1 
                    max_val = node.val 
                if node.left:
                    queue.append([node.left, max_val])
                if node.right:
                    queue.append([node.right, max_val])

        return count 

            