class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = {}
        for i in range(numCourses):
            graph[i] = []

        for a, b in prerequisites:
            graph[b].append(a)

        finished = set()
        current = set()
        cycle = False

        stack = []

        def dfs(i):
            nonlocal cycle

            neighbors = graph.get(i, [])
            current.add(i)
            for n in neighbors:
                if n in current:
                    cycle = True 
                    return 
                if n in finished:
                    continue 
                dfs(n)

            stack.append(i)
            current.discard(i)
            finished.add(i)

        for i in range(numCourses):
            if i in finished: continue 
            dfs(i)

        return stack[::-1] if not cycle else []