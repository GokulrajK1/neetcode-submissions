class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        res = [-1] * len(queries)

        graph = defaultdict(list)
        for i, (a, b) in enumerate(equations):
            graph[a].append((b, values[i]))
            graph[b].append((a, 1 / values[i]))

        for i, (x, y) in enumerate(queries):

            if x not in graph: continue 

            queue = deque([(x, 1)])
            visited = set([x])

            while queue:
                n, total = queue.popleft()
                if n == y: 
                    res[i] = total 
                    break 

                for c, v in graph[n]:
                    if c in visited: continue 
                    visited.add(c)
                    queue.append((c, total * v))

        return res