class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(i,currSum):
            if (i,currSum) in memo:
                return memo[(i,currSum)]
            if i ==len(nums) and currSum == target:
                return 1
            
            if i >= len(nums):
                return 0
            
            # to include neg
            memo[(i,currSum)] = dfs(i+1,currSum+nums[i]) + dfs(i+1,currSum +(-nums[i]))

            
            return memo[(i,currSum)]
        
        return dfs(0,0)
            