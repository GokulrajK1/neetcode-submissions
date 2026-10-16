"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i : i.start)
        res = []
        for interval in intervals:
            if res and res[-1].end > interval.start:
                return False

            res.append(interval)

        return True 