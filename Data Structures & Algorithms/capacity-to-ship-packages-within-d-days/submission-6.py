class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lo = max(weights)
        hi = sum(weights)
        res = sum(weights)
        print(lo, hi)
        while lo <= hi:
            capacity = lo + (hi - lo) // 2
            print(capacity)
            total = 0
            d = 0 
            for weight in weights:
                if total + weight > capacity:
                    d += 1 
                    total = 0 
                total += weight 

            d += 1

            print(d)
            if d > days:
                lo = capacity + 1
            else:
                res = capacity
                hi = capacity - 1 

        return res 
