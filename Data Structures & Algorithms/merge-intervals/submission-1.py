class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        for interval in intervals:
            if len(res) > 0 and res[-1][1] >= interval[0]:
                old = res.pop()
                res.append([min(interval[0], old[0]), max(interval[1], old[1])])
            else:
                res.append(interval)

        return res