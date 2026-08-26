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
            level = []
            for _ in range(len(queue)):
                node = queue.popleft() 
                level.append(node.val if node else None)
                if node == None:
                    continue
                queue.append(node.left)
                queue.append(node.right)

            res.extend(level)



        return "|".join(str(x) if x else "N" for x in res)

            

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes_list = data.split("|")
        print(nodes_list)
        if len(nodes_list) < 1 or nodes_list[0] == "N":
            return None

        head = TreeNode(nodes_list[0])
        queue = deque([head])
     
        for i in range(1, len(nodes_list) - 1, 2):
            if len(queue) == 0:
                break
            root = queue.popleft()
            
            root.left = TreeNode(nodes_list[i]) if nodes_list[i] != "N" else None 
            root.right = TreeNode(nodes_list[i + 1]) if nodes_list[i + 1] != "N" else None 
            print(root.val, root.left.val if root.left else None, root.right.val if root.right else None)
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)

        return head
