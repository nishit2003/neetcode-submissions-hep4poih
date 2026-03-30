class Solution:
    def climbStairs(self, n: int) -> int:
        # iterative
        # one, two = 1,1
        # for i in range(n-1):
        #     temp = one
        #     one = one+two
        #     two = temp
        # return one

        # dp
        # dp = [0] * (n+1)
        # dp[0] = 1
        # dp[1] = 1
        # for i in range(2,n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n]
    
        # recurisve
        def dfs(i):
            if i >= n:
                return i == n
            return dfs(i+1) + dfs(i+2)
        
        return dfs(0)