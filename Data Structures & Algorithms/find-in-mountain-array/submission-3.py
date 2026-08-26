class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        total_length = mountainArr.length()

        cache = {}

        def get(i):
            if i not in cache:
                cache[i] = mountainArr.get(i)
            return cache[i]

        
        lo = 0 
        hi = total_length - 1
        half = -1 
        while lo <= hi:
            mid = lo + (hi - lo) // 2 
            mid_num = get(mid)
            mid_left_num = get(mid - 1) if mid > 0 else float("-inf")
            mid_right_num = get(mid + 1) if mid + 1 < total_length else float('inf')

            if mid_left_num <= mid_num and mid_num <= mid_right_num:
                lo = mid + 1
            elif mid_left_num >= mid_num and mid_num >= mid_right_num:
                hi = mid - 1
            else:
                half = mid 
                break 

        lo = 0 
        hi = half 
        while lo <= hi:
            mid = lo + (hi - lo) // 2 
            mid_num = get(mid)
            
            if target > mid_num:
                lo = mid + 1 
            elif target < mid_num:
                hi = mid - 1 
            else:
                return mid 

        lo = half + 1 
        hi = total_length - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            mid_num = get(mid)
          
            if target > mid_num:
                hi = mid - 1 
            elif target < mid_num:
                lo = mid + 1 
            else:
                return mid 

        return -1 