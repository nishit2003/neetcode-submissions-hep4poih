class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) // 2
        if sum(nums) % 2 != 0:
            return False
        memo = {}
        def helper(i, currsum):
            if (i,currsum) in memo:
                return memo[(i,currsum)]
            if currsum == target:
                return True

            if i >= len(nums) or currsum > target:
                return False
            
            # to inlcude 
            memo[(i,currsum)] = helper(i+1,currsum+nums[i]) or helper(i+1, currsum)       
            return memo[(i,currsum)]
        return helper(0,0)

