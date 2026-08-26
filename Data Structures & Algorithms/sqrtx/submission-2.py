class Solution:
    def mySqrt(self, x: int) -> int:
        lo = 1 
        hi = x 
        ans = 0
        while lo <= hi:
            mid = lo + (hi - lo) // 2 
            if x < mid * mid:
                hi = mid - 1 
            elif x > mid * mid:
                ans = mid
                lo = mid + 1 
            else:
                return mid
        return ans       