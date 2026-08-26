class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Top Down
        n = len(nums)
        def backtrack(i, remaining, memo):
            if (i, remaining) in memo:
                print("fire", (i, remaining))
                return memo[(i, remaining)]

            if remaining == target and i == n: 
                return 1 

            if i == n:
                return 0 

            print("START", i, nums[i], remaining)

            memo[(i + 1, remaining + nums[i])] = backtrack(i + 1, remaining + nums[i], memo) 
            print("He", memo[(i + 1, remaining + nums[i])], (i + 1, remaining + nums[i]))
            print("FIRST", i, nums[i], remaining)
            memo[(i + 1, remaining - nums[i])] = backtrack(i + 1, remaining - nums[i], memo)
            print("Ha", memo[(i + 1, remaining - nums[i])], (i + 1, remaining - nums[i]))
            print("SECOND", i, nums[i], remaining)
            return memo[(i + 1, remaining + nums[i])] + memo[(i + 1, remaining - nums[i])]

        return backtrack(0, 0, {})