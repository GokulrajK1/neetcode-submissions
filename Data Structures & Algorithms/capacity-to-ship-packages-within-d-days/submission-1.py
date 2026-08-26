class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        lo = max(weights) 
        hi = sum(weights)
        ans = 0
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            d = 1
            curr = 0
            for weight in weights:
                if curr + weight > mid:
                    d += 1 
                    curr = 0
                curr += weight

            if d <= days:
                ans = mid 
                hi = mid - 1
            else:
                lo = mid + 1

        return ans
            
            


