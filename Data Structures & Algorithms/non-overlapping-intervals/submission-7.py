class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        res = []
        intervals.sort(key = lambda i : i[-1])
        for i, interval in enumerate(intervals):
            if res and res[-1][1] > interval[0]:
                count += 1
                continue 
            res.append(interval)

        return count 