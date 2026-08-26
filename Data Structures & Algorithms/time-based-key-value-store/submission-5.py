class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        values = self.store.get(key, [])
        values.append([timestamp, value])
        self.store[key] = values
      

    def get(self, key: str, timestamp: int) -> str:
        print(self.store)
        if key not in self.store:
            return ""
        
        lo = 0
        res = -1
        hi = len(self.store[key]) - 1 
        values = self.store[key]
      
        while lo <= hi:
            mid = lo + (hi - lo) // 2 
            if values[mid][0] < timestamp:
                res = mid 
                lo = mid + 1 
            elif values[mid][0] > timestamp:
                hi = mid - 1 
            else:
                return values[mid][1]

        if res == -1:
            return ""
            
        return values[res][1]

        
