class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total %2 != 0:
            return False
        target = total // 2
        memo = {}
        def dfs(i,curr):
            if (i,curr) in memo:
                return memo[(i,curr)]
            if curr == target:
                return True
            if curr > target or i >= len(nums):
                return False

            # we choose
            choose = dfs(i+1,curr+nums[i])

            # we choose not to add
            skip = dfs(i+1,curr)
            memo[(i,curr)] =  choose or skip
            return memo[(i,curr)]
        return dfs(0,0)

