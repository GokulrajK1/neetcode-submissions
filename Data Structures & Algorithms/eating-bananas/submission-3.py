class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo_k = 1 
        hi_k = max(piles)
        res = 1 
        while lo_k <= hi_k: 
            k = lo_k + (hi_k - lo_k) // 2 
            h_val = 0
            for pile in piles:
                h_val += pile // k + (0 if pile % k == 0 else 1)
            if h_val <= h:
                res = k 
                hi_k = k - 1 
            else:
                lo_k = k + 1 

        return res 

        