class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda x : x[0])
        print(intervals)
        i = 0 
        res = [-1] * len(queries)
        min_dist_heap = []
        queries = sorted(((i, val) for i, val in enumerate(queries)), key = lambda x : x[1])
        for j, query in queries:
            print(query, i)
            while i < len(intervals) and intervals[i][0] <= query:
                start, end = intervals[i]
                heapq.heappush(min_dist_heap, (end - start + 1, (start, end)))
                i += 1 
            print(min_dist_heap)
            while min_dist_heap and min_dist_heap[0][1][1] < query:
                heapq.heappop(min_dist_heap)
            
            if min_dist_heap:
                res[j] = min_dist_heap[0][0]

        return res 
                

        