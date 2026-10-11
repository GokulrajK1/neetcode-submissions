class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        values = self.store.get(key, [])
        values.append((timestamp, value))
        self.store[key] = values

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store: return ""
        lo = 0
        hi = len(self.store[key]) - 1
        res = ""
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if self.store[key][mid][0] <= timestamp:
                res = self.store[key][mid][1]
                lo = mid + 1
            else:
                hi = mid - 1

        return res
