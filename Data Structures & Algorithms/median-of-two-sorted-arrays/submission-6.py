class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A

        total = len(nums1) + len(nums2)
        half = total // 2

        lo = 0
        hi = len(A) - 1

        while True:
            midA = lo + (hi - lo) // 2
            midB = half - midA - 2

            leftA = A[midA] if midA >= 0 else float("-inf")
            rightA = A[midA + 1] if midA + 1 < len(A) else float("inf")

            leftB = B[midB] if midB >= 0 else float("-inf")
            rightB = B[midB + 1] if midB + 1 < len(B) else float('inf')

            if leftB > rightA:
                lo = midA + 1
            elif leftA > rightB:
                hi = midA - 1
            else:
                if total % 2 == 0:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2

                return min(rightA, rightB)

                