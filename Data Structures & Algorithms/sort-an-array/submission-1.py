class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        hi = len(nums) - 1 
        self.merge_sort(0, hi, nums)
        return nums

    def merge_sort(self, lo, hi, nums):
        if lo < hi:
            mid = (lo + hi) // 2 
            self.merge_sort(lo, mid, nums)
            self.merge_sort(mid + 1, hi, nums)
            self.merge(lo, mid, hi, nums)

    def merge(self, lo, mid, hi, nums):
        list_A = nums[lo:mid+1]
        list_B = nums[mid+1:hi+1]
        i, j, k = 0, 0, lo
        print(hi - lo + 1)
        while k < hi + 1:
            if i < mid + 1 - lo and j < hi - mid:
                if list_A[i] > list_B[j]:
                    nums[k] = list_B[j]
                    j += 1 
                else:
                    nums[k] = list_A[i]
                    i += 1 
            elif i < mid + 1 - lo:
                nums[k] = list_A[i]
                i += 1 
            else:
                nums[k] = list_B[j]
                j += 1 
            k += 1 
