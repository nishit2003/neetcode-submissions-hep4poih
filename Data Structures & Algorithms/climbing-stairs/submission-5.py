class Solution:
    def climbStairs(self, n: int) -> int:
        
        # def dfs(i):
        #     if i >= n:
        #         return i == n
        #     return dfs(i+1) + dfs(i+2)

        # for i in range(n):
        #     return dfs(i) 

        curr, prev = 1,1

        for step in range(n):
            temp = curr + prev
            curr = prev
            prev = temp
        return curr