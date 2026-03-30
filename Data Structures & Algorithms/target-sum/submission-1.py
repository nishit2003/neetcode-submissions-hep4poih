class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        


        def dfs(i,currSum):
            if i ==len(nums) and currSum == target:
                return 1
            
            if i >= len(nums):
                return 0
            
            # to include neg
            res = dfs(i+1,currSum+nums[i]) + dfs(i+1,currSum +(-nums[i]))

            # to include pos
            
            return res
        
        return dfs(0,0)
            