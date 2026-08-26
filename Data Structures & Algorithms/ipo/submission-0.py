class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capitals_list = sorted([(capital, profit) for capital, profit in zip(capital, profits)], key=lambda x : x[0])
        i = 0 
        profits_heap = []
        count = 0 
        curr = w 

        print("CL", capitals_list)

        while i < len(capitals_list) or profits_heap:

            while i < len(capitals_list) and curr >= capitals_list[i][0]:
                capital, profit = capitals_list[i]
                heapq.heappush(profits_heap, (-profit, capital))
                i += 1 

            print("PH", profits_heap)
            
            if profits_heap:
                profit, capital = heapq.heappop(profits_heap)
                curr += -profit 
                count += 1 
                print("Curr, Count", curr, count)
                if count == k:
                    break
            else:
                break 

        return curr 

