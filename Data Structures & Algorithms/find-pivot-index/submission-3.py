class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        prefix = [0] * (len(nums) + 1)

        for i in range(1,len(nums)+1):
            prefix[i] = prefix[i-1] + nums[i-1]
        print(prefix)
        
        for i in range(len(nums)):
            left = prefix[i]
            right = total - prefix[i] - nums[i]
            if left == right:
                return i 

        return -1