class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        output = [1] * n
        
        # 1. Left pass: output[i] contains the product of all elements to the left
        left_product = 1
        for i in range(n):
            output[i] = left_product
            left_product *= nums[i]
            
        # 2. Right pass: multiply with the product of all elements to the right
        right_product = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]
            
        return output