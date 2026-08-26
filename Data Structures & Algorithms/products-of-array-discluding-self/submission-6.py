class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        products = [1] * n
        for i in range(1, n):
            products[i] = nums[i - 1] * products[i - 1]

        prefix = nums[n - 1]
        for i in range(n - 2, -1, -1):
            products[i] *= prefix 
            prefix *= nums[i]

        return products
           


        print(products)
