class Solution:
    def climbStairs(self, n: int) -> int:
        
        def dfs(i):
            if i >= n:
                return i == n
            return dfs(i+1) + dfs(i+2)

        for i in range(n):
            return dfs(i) 