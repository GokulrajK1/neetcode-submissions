class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(nums, lo, mid, hi):
            nums1 = nums[lo:mid+1]
            nums2 = nums[mid+1:hi+1]
            
            i, j, k = 0, 0, lo
            while i < len(nums1) and j < len(nums2):
                
                if nums1[i] > nums2[j]:
                    nums[k] = nums2[j]
                    j += 1 
                else:
                    nums[k] = nums1[i]
                    i += 1 

                k += 1 

            while i < len(nums1):
                nums[k] = nums1[i]
                k += 1 
                i += 1 

            while j < len(nums2):
                nums[k] = nums2[j]
                k += 1 
                j += 1 

        
        def mergesort(nums, lo, hi):

            if hi - lo < 1:
                return 

            mid = lo + (hi - lo) // 2 
            mergesort(nums, lo, mid)
            mergesort(nums, mid + 1, hi)
            
            merge(nums, lo, mid, hi)

        mergesort(nums, 0, len(nums) - 1)

        return nums 

        
        
