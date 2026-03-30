class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2

        def dfs(i,currSum):
            if currSum == target:
                return True

            if i >= len(nums) or currSum > target:
                return False
            
            # to not include
            res = dfs(i+1,currSum)

            # to include
            resNot = dfs(i+1,currSum+nums[i])

            return resNot or res
        return dfs(0,0)