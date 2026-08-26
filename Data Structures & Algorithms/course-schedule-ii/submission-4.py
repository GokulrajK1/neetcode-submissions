class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        for a, b in prerequisites:
            graph[a].append(b)

        current = set()
        finished = set()
        order = []
        cycle = False

        def dfs(node):
            nonlocal cycle

            current.add(node)

            print(node, graph[node], "i")
            
            for n in graph[node]:
                if n in current: 
                    cycle = True
                    return
                if n in finished:
                    continue
                
                print("nod", node)
                dfs(n)
                    

            order.append(node)
            current.remove(node)
            finished.add(node)
    

        for i in range(numCourses):
            if i in graph and i not in finished:
                dfs(i)

        if cycle: return []
        return order
            