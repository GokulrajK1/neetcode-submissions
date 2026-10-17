class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        parent = {}
        weight = {}

        def find(u):
            if u != parent[u]:
                root = find(parent[u])
                weight[u] *= weight[parent[u]]
                parent[u] = root

            return parent[u]

        def union(u, v, value):
            if u not in parent:
                parent[u] = u
                weight[u] = 1

            if v not in parent:
                parent[v] = v
                weight[v] = 1

            ru, rv = find(u), find(v)
            if ru != rv:
                parent[ru] = rv
                weight[ru] = value * (weight[v] / weight[u])
        for i in range(len(equations)):
            union(equations[i][0], equations[i][1], values[i])

        res = []

        for x, y in queries:
            if x not in parent or y not in parent or find(x) != find(y):
                res.append(-1)
                continue 
                
            res.append(weight[x] / weight[y]) 

        return res