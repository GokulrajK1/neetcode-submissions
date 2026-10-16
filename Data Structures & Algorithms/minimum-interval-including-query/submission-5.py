class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        queries = [(q, i) for i, q in enumerate(queries)]
        queries.sort()
        intervals.sort()
        index = 0 
        lengths = []
        output = [-1] * len(queries)

        for query, j in queries:
            while index < len(intervals) and intervals[index][0] <= query:
                i = intervals[index]
                heapq.heappush(lengths, (i[1] - i[0] + 1, i))
                index += 1

            while lengths and lengths[0][1][1] < query:
                heapq.heappop(lengths)

            if lengths:
                output[j] = lengths[0][0]

        return output




