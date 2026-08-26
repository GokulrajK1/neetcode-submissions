class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()

        def permute(curr, numbers):
            nonlocal res, nums

            if len(curr) == len(nums):
                res.append(curr.copy())

            for i in range(len(numbers)):
                if i > 0 and numbers[i] == numbers[i - 1]:
                    print("Hello", numbers[i])
                    continue 

                curr.append(numbers[i])
                permute(curr.copy(), numbers[:i] + numbers[i+1:])
                curr.pop()

        permute([], nums)
        return res