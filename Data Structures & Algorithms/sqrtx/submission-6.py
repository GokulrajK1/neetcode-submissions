class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        lo = 0 
        hi = x // 2 
        res = 0 
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if mid * mid < x:
                res = mid 
                lo = mid + 1
            elif mid * mid > x:
                hi = mid - 1
            else:
                return mid 

        return res