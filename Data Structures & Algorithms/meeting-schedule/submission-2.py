"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x : x.end)
        for i in range(1, len(intervals)):
            m1, m2 = intervals[i - 1], intervals[i]
            if m1.end > m2.start:
                return False

        return True 