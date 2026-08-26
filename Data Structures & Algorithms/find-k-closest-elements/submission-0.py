class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0 
        for right in range(len(arr)):
            if right - left + 1 > k:
                if abs(arr[left] - x) <= abs(arr[right] - x):
                    return arr[left:right]
                else:
                    left += 1 

        return arr[left:]
