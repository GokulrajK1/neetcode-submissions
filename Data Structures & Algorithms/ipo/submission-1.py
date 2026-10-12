class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = [(c, i) for i, (c, p) in enumerate(zip(capital, profits))]
        available = []
        heapq.heapify(projects)
        pnl = w
        count = 0
        while projects or available:
            while projects and projects[0][0] <= pnl:
                c, i = heapq.heappop(projects)
                heapq.heappush(available, -profits[i])

            if available:
                count += 1 
                pnl += -heapq.heappop(available)
            else:
                break

            if count == k:
                break 



        return pnl


