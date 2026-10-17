class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {}
        for i in range(numCourses):
            graph[i] = []

        for a, b in prerequisites:
            graph[b].append(a)

        finished = set()
        current = set()

        def dfs(i):
           
            neighbors = graph.get(i, [])
            current.add(i)
            for n in neighbors:

                if n in finished: continue 
                if n in current: return False 

                if not dfs(n): return False

            current.discard(i)
            finished.add(i)
            return True 

        for i in range(numCourses):
            if i in finished: continue 
            if not dfs(i): return False

        return True
