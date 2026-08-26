class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if len(weights) <= days:
            return max(weights)

        lo = 1 
        hi = 500 * 500000
        ans = 0
        max_weight = max(weights)
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

            if d <= days:
                ans = mid 
                hi = mid - 1
            else:
                lo = mid + 1

        return ans
            
            


