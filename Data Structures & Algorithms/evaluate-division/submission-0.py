class Solution:
    def generate_graph(self, equations, values):
        graph = {}
        for equation, value in zip(equations, values):
            graph[equation[0]] = graph.get(equation[0], []) + [(equation[1], value)] + [(equation[0], 1.0)]
            graph[equation[1]] = graph.get(equation[1], []) + [(equation[0], 1 / value)] + [(equation[1], 1.0)]

        return graph

    def search(self, src, dst, graph):
        if src == dst and src not in graph:
            return -1.0
        stack = [(src, 1)]
        seen = set()
        while stack:
            node, cost = stack.pop()

            if node in seen:
                continue

            print(f"Node: {node}")

            if node == dst:
                graph[src] = graph.get(src, []) + [(dst, cost)]
                graph[dst] = graph.get(dst, []) + [(src, 1 / cost)]
               
                return cost

            seen.add(node)

            neighbors = graph.get(node, [])
            for neighbor in neighbors:
                stack.append((neighbor[0], cost * neighbor[1]))

        return -1.0

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = self.generate_graph(equations, values)
        print(graph)
        res = []
        for query in queries:
            res.append(self.search(query[0], query[1], graph))

        return res

