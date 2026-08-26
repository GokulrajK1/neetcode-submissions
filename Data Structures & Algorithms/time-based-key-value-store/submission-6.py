class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []

        self.store[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])
        lo = 0
        hi = len(values) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if values[mid][0] <= timestamp:
                res = values[mid][1]
                lo = mid + 1 
            else:
                hi = mid - 1 

        return res

        
