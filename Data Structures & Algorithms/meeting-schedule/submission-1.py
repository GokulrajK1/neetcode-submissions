"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True 
        intervals.sort(key = lambda x : x.end)
        endTime = intervals[0].end
        for i in range(1, len(intervals)):
            if endTime > intervals[i].start:
                return False 
            endTime = intervals[i].end

        return True 