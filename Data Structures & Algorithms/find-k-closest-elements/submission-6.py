class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        i = 0 
        for j in range(len(arr)):
            while i < j and j - i + 1 > k:
                if abs(arr[i] - x) > abs(arr[j] - x) or arr[j] == arr[i]:
                    i += 1 
                else:
                    return arr[i:j]
        
        return arr[i:]