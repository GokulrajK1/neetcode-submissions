class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lo = 1 
        hi = 500 * 500000
        max_weight = max(weights)
        res = hi 
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if mid < max_weight:
                lo = mid + 1 
                continue 
            d = 1
            curr = 0
            for weight in weights:
                if curr + weight > mid:
                    d += 1 
                    curr = 0
                curr += weight

            print(mid, d)

            if d > days:
                lo = mid + 1 
            else:
                res = mid 
                hi = mid - 1 

            
        return res


