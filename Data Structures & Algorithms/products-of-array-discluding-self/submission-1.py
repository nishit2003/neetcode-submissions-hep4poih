from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        res = [1] * len(nums)  # Initialize result array with 1s

        # Step 1: Calculate prefix products
        for i in range(len(nums)):
            res[i] = prefix  # Store the current prefix product in res
            prefix *= nums[i]  # Update prefix product
        
        postfix = 1
        # Step 2: Calculate postfix products and update the result array
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix  # Multiply the current value in res by postfix
            postfix *= nums[i]  # Update postfix product

        return res
