class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False 

        target = total // k 
        sums = [0] * k 

        nums.sort(reverse=True)

        def backtrack(i):

            if i == len(nums):
                return sums.count(sums[0]) == len(sums)

            seen = set()

            for j in range(k):

                if sums[j] in seen:
                    continue 

                if sums[j] + nums[i] > target:
                    continue 

                sums[j] += nums[i]
                res = backtrack(i + 1)
                sums[j] -= nums[i]

                if res:
                    return True

                if sums[j] == 0:
                    break 

            return False 

        return backtrack(0)