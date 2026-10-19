class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        row_graph = {}
        for i in range(1, k + 1):
            row_graph[i] = []

        for a, b in rowConditions:
            row_graph[a].append(b)

        col_graph = {}
        for i in range(1, k + 1):
            col_graph[i] = []

        for a, b in colConditions:
            col_graph[a].append(b)

        stack = []
        current = set()
        finished = set()

        def dfs(node, graph):

            current.add(node)
            for neighbor in graph[node]:
                if neighbor in finished:
                    continue
                if neighbor in current:
                    return False 
                if not dfs(neighbor, graph):
                    return False

            current.discard(node)
            finished.add(node)
            stack.append(node)

            return True

        for i in range(1, k + 1):
            if i in finished: 
                continue
            if not dfs(i, row_graph):
                return []

        row_ordering = stack[::-1]

        stack = []
        current = set()
        finished = set()

        for i in range(1, k + 1):
            if i in finished: 
                continue
            if not dfs(i, col_graph):
                return []

        col_ordering = stack[::-1]

        row_index = {node : index for index, node in enumerate(row_ordering)}
        col_index = {node : index for index, node in enumerate(col_ordering)}

        matrix = [[0] * k for _ in range(k)]

        for node in range(1, k + 1):
            i, j = row_index[node], col_index[node]
            if matrix[i][j] != 0: return []
            matrix[i][j] = node

        return matrix
