class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1: return 1

        if len(arr) == 2:
            return 2 if arr[0] > arr[1] or arr[1] > arr[0] else 1

        max_length = 1
        start = 0

        for i in range(len(arr) - 2):
            if arr[i] > arr[i + 1] < arr[i + 2] or arr[i] < arr[i + 1] > arr[i + 2]:
                print(i, arr[i], start)
                max_length = max(max_length, i + 2 - start + 1)
            elif arr[i] > arr[i + 1] or arr[i] < arr[i + 1] or arr[i + 1] > arr[i + 2] or arr[i + 1] < arr[i + 2]:
                max_length = max(max_length, 2)
                start = i + 1
            else:
                start = i + 1

        return max_length

