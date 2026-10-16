"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []
        
        for interval in intervals:
            events.append((interval.start, 1))
            events.append((interval.end, -1))

        events.sort(key = lambda event : (event[0], event[1]))
        max_roms = 0
        curr = 0
        for event in events:
            curr += event[1]
            max_roms = max(curr, max_roms)

        return max_roms
