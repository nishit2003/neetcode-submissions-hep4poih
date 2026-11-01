class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        # dp = [0] * (n+1)
        # dp[1] = 1
        # dp[2] = 2
        # for i in range(3,n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        
        # return dp[n]

        memo = {}
        def dfs(n):
            if n <= 2:
                return n
            if n in memo:
                return memo[n]
            memo[n] =  dfs(n-1) + dfs(n-2)
            return memo[n]
        return dfs(n)
# DP = [0,1,2,i-2+i-2]