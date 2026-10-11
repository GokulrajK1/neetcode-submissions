class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        lo = 0
        hi = mountainArr.length() - 1
        pivot = lo
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            left = mountainArr.get(mid - 1) if mid - 1 >= 0 else float("-inf")
            middle = mountainArr.get(mid)
            right = mountainArr.get(mid + 1) if mid + 1 < mountainArr.length() else float("inf")

            if left < middle and middle < right:
                lo = mid + 1
            elif left > middle and middle > right:
                hi = mid - 1
            else:
                pivot = mid 
                break 

        lo = 0
        hi = pivot 
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if mountainArr.get(mid) < target:
                lo = mid + 1
            elif mountainArr.get(mid) > target:
                hi = mid - 1
            else:
                return mid 

        lo = pivot + 1
        hi = mountainArr.length() - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if mountainArr.get(mid) < target:
                hi = mid - 1
            elif mountainArr.get(mid) > target:
                lo = mid + 1
            else:
                return mid 

        return -1


        