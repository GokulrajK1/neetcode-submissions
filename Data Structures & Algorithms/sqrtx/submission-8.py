class Solution:
    def mySqrt(self, x: int) -> int:
   
        lo = 0 
        hi = x
        res = 1 
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