class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # m,n = rows, cols
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[m-1][n-1] = 1
        # down, right = 0,0 

        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):
                down = dp[r+1][c] if r+1 < m else 0
                right = dp[r][c+1] if c+1 < n else 0
                dp[r][c] = dp[r][c] + down + right
        return dp[0][0]

