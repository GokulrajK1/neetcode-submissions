class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r = len(heights)
        c = len(heights[0])
        p_list = [(i, j) for i in range(r) for j in range(c) if i == 0 or j == 0]
        a_list = [(i, j) for i in range(r) for j in range(c) if i == r - 1 or j == c - 1]

        p_set = set()
        a_set = set()

        def dfs(x, y, seen):
            if (x, y) in seen:
                return 

            seen.add((x, y))
            if x + 1 <= r - 1 and heights[x + 1][y] >= heights[x][y]:
                dfs(x + 1, y, seen)
            if x - 1 >= 0 and heights[x - 1][y] >= heights[x][y]:
                dfs(x - 1, y, seen)
            if y + 1 <= c - 1 and heights[x][y + 1] >= heights[x][y]:
                dfs(x, y + 1, seen)
            if y - 1 >= 0 and heights[x][y - 1] >= heights[x][y]:
                dfs(x, y - 1, seen)


        for i, j in p_list:
            dfs(i, j, p_set)

        for i,j in a_list:
            dfs(i, j, a_set)

       
        return list(p_set & a_set)

            


                    
