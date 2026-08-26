class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo_k = 1
        hi_k = max(piles)
        res = -1 
        while lo_k <= hi_k:
            mid_k = lo_k + (hi_k - lo_k) // 2
            hours = 0 
            for pile in piles:
                hours += pile // mid_k + (1 if pile % mid_k != 0 else 0)

            if hours > h:
                lo_k = mid_k + 1 
            else:
                res = mid_k 
                hi_k = mid_k - 1 

        return res 
