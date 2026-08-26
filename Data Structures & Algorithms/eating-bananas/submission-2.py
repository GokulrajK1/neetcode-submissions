import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)
        ans = 0
        while lo <= hi:
            mid = lo + (hi - lo) // 2 
            hrs = 0
            print("boo")
            for pile in piles:
                hrs += math.ceil(pile / mid)
                print(hrs)
            if hrs > h:
                lo = mid + 1 
            elif hrs <= h:
                ans = mid 
                hi = mid - 1 

        print("hello")
        return ans  
