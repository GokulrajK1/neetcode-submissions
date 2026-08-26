class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key] = self.time_map.get(key, []) + [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        values = self.time_map.get(key)
        if values is None:
            return ""
        lo = 0
        hi = len(values) - 1 
        ans = -1 
        while lo <= hi:
            mid = lo + (hi - lo) // 2 
            if values[mid][1] <= timestamp:
                ans = mid 
                lo = mid + 1
            else:
                hi = mid - 1

        if ans == -1:
            return ""

        return values[ans][0]
