class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        target = sum(nums) // 2
        n = len(nums)
        memo = {}
        def dfs(i,target):
            if (i,target) in memo:
                return memo[(i,target)]
            if target == 0:
                return True
            if i >= n or target < 0:
                return False
            # valid index and include the next num or (not include)
            memo[(i,target)] = dfs(i+1,target - nums[i]) or dfs(i+1,target)
            return memo[(i,target)]
        return dfs(0, target)
            

