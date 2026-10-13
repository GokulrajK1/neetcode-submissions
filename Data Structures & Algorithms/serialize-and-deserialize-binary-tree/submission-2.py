# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        queue = deque([root])
        res = []

        while queue:
       
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)

                res.append(node.val if node else None)

        return "|".join(str(x) if x else "N" for x in res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        nodes_list = data.split("|")
        if len(nodes_list) < 1 or nodes_list[0] == "N": return None

        root = TreeNode(int(nodes_list[0]))
        queue = deque([root])

        for i in range(1, len(nodes_list), 2):
            node = queue.popleft()
            node.left = TreeNode(int(nodes_list[i])) if nodes_list[i] != "N" else None
            node.right = TreeNode(int(nodes_list[i + 1])) if nodes_list[i + 1] != "N" else None
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root 



