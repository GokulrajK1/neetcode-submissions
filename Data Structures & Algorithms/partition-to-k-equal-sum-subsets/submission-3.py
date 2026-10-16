class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        total = sum(nums)
        if total % k != 0: return False

        side = total // k 
        if max(nums) > side:
            return False 

        piles = [0] * k
        count = 0

        ans = False 

        nums.sort(reverse=True)

        def backtrack(i):

            if i == len(nums):
                return True 

            seen = set()

            for j in range(len(piles)):
                if piles[j] + nums[i] > side or piles[j] in seen:
                    continue 

                seen.add(piles[j])
                
                piles[j] += nums[i]

                if backtrack(i + 1):
                    return True

                piles[j] -= nums[i]

            return False 

        return backtrack(0)

  

        

