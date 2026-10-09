class Solution:

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        i = 0 
        for j in range(len(arr)):

            if j - i + 1 > k and (abs(arr[j] - x) < abs(arr[i] - x) or arr[i] == arr[j]):
                i += 1

            elif j - i + 1 > k:
                return arr[i:j]

        return arr[i:]

            
