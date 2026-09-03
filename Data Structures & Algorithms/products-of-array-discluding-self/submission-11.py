class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    # prefix = [1,1,2,8]
    # suffix = [48,24,6,1]
    # res = [48,24,12,8]
        res = [1] * len(nums)
        prefix = [1] * len(nums) #[1,1,2,8]

        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1]*nums[i-1]
        
        suffix = [1] * len(nums) #[1,1,1,1]
        for i in range(len(nums)-2,-1,-1):
            suffix[i] = suffix[i+1] * nums[i+1]

        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[i]
        
        return res