class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = {}
        def dfs(total):
            if total == target:
                return 1
            if total > target:
                return 0
            
            if total in dp:
                return dp[total]

            ways = 0 
            for num in nums:
                ways+=dfs(num+total)
            
            dp[total] = ways
            return ways
        return dfs(0)