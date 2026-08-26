class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        if len(nums) <= 5:
            return sorted(nums, reverse=True)[k - 1]
        
        medians = []
        for i in range(0, len(nums), 5):
            group = nums[i:i+5]
            group.sort()
            medians.append(group[len(group) // 2])

        pivot = self.findKthLargest(medians, (len(medians) + 1)//2)

        greater = [x for x in nums if x > pivot]
        equal   = [x for x in nums if x == pivot]
        less    = [x for x in nums if x < pivot]

        if k <= len(greater):
            return self.findKthLargest(greater, k)
        elif k <= len(greater) + len(equal):
            return pivot
        else:
            return self.findKthLargest(less, k - len(greater) - len(equal))


        


        # nums = [-x for x in nums]
        # heapq.heapify(nums)
        # count = 0 
        # print(nums)
        # res = None
        # while len(nums) > 0 and count < k:
        #     count += 1 
        #     res = heapq.heappop(nums)

        # return -res