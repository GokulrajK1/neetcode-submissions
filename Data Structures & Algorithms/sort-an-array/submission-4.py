class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge_sort(0, len(nums) - 1, nums)
        return nums

    def merge_sort(self, lo, hi, nums):
        if lo < hi:
            mid = (lo + hi) // 2
            self.merge_sort(lo, mid, nums)
            self.merge_sort(mid + 1, hi, nums)
            self.merge(lo, mid, hi, nums)
        

    def merge(self, lo, mid, hi, nums):
        array = []
        i = lo
        j = mid + 1 
       
        while True:
            if i > mid and j > hi:
                break
            elif i > mid:
                array.append(nums[j])
                j += 1
            elif j > hi:
                array.append(nums[i])
                i += 1 
            else:
                if nums[i] < nums[j]:
                    array.append(nums[i])
                    i += 1
                else:
                    array.append(nums[j])
                    j += 1 

        for i in range(len(array)):
            nums[lo + i] = array[i]

                
    
    


