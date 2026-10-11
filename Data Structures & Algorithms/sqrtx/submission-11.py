class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        lo = 1
        hi = x // 2 
        res = lo
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if mid * mid > x:
                hi = mid - 1 
            elif mid * mid < x:
                res = mid
                lo = mid + 1
            else:
                return mid 

        return res