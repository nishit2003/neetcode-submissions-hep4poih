class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2!= 0:
            return False
        target = total // 2
        memo = {}
        def dfs(i,currsum):
            if (i,currsum) in memo:
                return memo[(i,currsum)]
            if currsum > target or i >= len(nums):
                return False
            
            if currsum == target:
                return True

            # we choose
            res = dfs(i+1,currsum+nums[i])

            # not choose
            resnot = dfs(i+1,currsum)
            memo[(i,currsum)] = res or resnot
            return memo[(i,currsum)]
        return dfs(0,0)
