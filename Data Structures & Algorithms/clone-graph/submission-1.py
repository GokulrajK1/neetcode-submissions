"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node: return None
        
        val_to_node = {1 : Node(1)}

        def dfs(old_node):
            if not old_node: return None
            new_node = val_to_node[old_node.val]
            new_neighbors = []
            val_to_node[old_node.val].neighbors = new_neighbors 
            for neighbor in old_node.neighbors:
                if neighbor.val in val_to_node:
                    new_neighbors.append(val_to_node[neighbor.val])
                    continue
                val_to_node[neighbor.val] = Node(neighbor.val)
                new_neighbors.append(val_to_node[neighbor.val])
                dfs(neighbor)

        dfs(node)
        return val_to_node[1]

            

