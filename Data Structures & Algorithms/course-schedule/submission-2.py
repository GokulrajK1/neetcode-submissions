class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        
        for a, b in prerequisites:
            graph[a].append(b)
        
        current = set()
        finished = set()
        
        def dfs(node):
            current.add(node)
     
            for n in graph[node]:
                if n in current:
                    return True 
                if n in finished:
                    continue

                if dfs(n):
                    return True

            current.remove(node)
            finished.add(node)
            return False 

        for node in graph:
            if dfs(node):
                return False 

        return len(finished) == numCourses