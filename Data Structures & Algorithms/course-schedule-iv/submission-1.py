class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = {}
        for i in range(numCourses):
            graph[i] = []

        for a, b in prerequisites:
            graph[a].append(b)

        reached = {}

        def dfs(i):
            
            if i in reached: return reached[i]
            seen = set()
            for neighbor in graph[i]:
                seen.add(neighbor)
                seen |= dfs(neighbor)

            reached[i] = seen
            return seen

        for i in range(numCourses):
            dfs(i)

        return [v in reached[u] for u, v in queries]

           

