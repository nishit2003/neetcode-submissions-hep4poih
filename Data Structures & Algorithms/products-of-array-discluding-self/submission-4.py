class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for i in range(len(nums))]
        postfix = [1 for i in range(len(nums))]
        res = [1 for i in range(len(nums))]
        
        prod = 1
        for i in range(len(nums)):
            prefix[i] = prod
            prod*= nums[i]
            
        prod2 = 1
        for i in range(len(nums)-1,-1,-1):
            postfix[i] = prod2
            prod2 *= nums[i]
        
        print(prefix,postfix)

        for i in range(len(nums)):
            res[i] = prefix[i] * postfix[i]
    
        return res

