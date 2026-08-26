class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        count = 0
        intervals.sort(key = lambda x : x[1])
        lastEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            if lastEnd > intervals[i][0]:
                count += 1 
            else:
                lastEnd = intervals[i][1]

        return count