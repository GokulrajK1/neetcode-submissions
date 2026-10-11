class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)
        res = hi

        while lo <= hi:
            k = lo + (hi - lo) // 2

            hours = 0
            for pile in piles:
                hours += pile // k + int(pile % k != 0)

            if hours > h:
                lo = k + 1 

            else:
                res = k
                hi = k - 1

        return res