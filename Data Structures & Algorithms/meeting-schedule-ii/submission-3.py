"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        min_end_time_heap = []
        res = 0
        a = [(i.start, i.end) for i in sorted(intervals, key = lambda x : x.end)]
        print(a)
      
        for interval in sorted(intervals, key = lambda x : x.start):
            if not min_end_time_heap or min_end_time_heap[0][0] > interval.start:
                print("EEE", (interval.start, interval.end))
                if min_end_time_heap:
                    print("He", min_end_time_heap[0])
                heapq.heappush(min_end_time_heap, (interval.end, interval.start))
                res += 1 
                
            else:
                heapq.heappop(min_end_time_heap)
                heapq.heappush(min_end_time_heap, (interval.end, interval.start))

        return res

            
