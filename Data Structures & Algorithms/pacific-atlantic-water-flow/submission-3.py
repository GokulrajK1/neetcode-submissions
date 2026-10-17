class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        m, n = len(heights), len(heights[0])

        p_queue = deque()
        a_queue = deque()

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    p_queue.append((i,j))
                if i == m - 1 or j == n - 1:
                    a_queue.append((i, j))
        
        def bfs(queue, visited):

            while queue:
                i, j = queue.popleft()

                visited.add((i,j))

                directions = [(1,0), (-1,0), (0,1), (0,-1)]

                for dx, dy in directions:
                    x, y = i + dx, j + dy 
                    if x < 0 or y < 0 or x >= m or y >= n: continue 
                    if (x, y) in visited: continue 
                    if heights[i][j] <= heights[x][y]: 
                        visited.add((x,y))
                        queue.append((x, y))

        p_visited = set()
        a_visited = set()

        bfs(p_queue, p_visited)
        bfs(a_queue, a_visited)

        return list(p_visited & a_visited)