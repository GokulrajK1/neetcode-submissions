class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        final = []
        for i, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                final.append(interval)
            elif interval[0] > newInterval[1]:
                final.append(newInterval)
                return final + intervals[i:]
            else:
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
        final.append(newInterval)

        return final

