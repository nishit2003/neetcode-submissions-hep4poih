class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        m,n = len(s), len(p)
        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if j == n:
                return i == m

            first = i < m and (s[i]==p[j] or p[j] == ".")
            if (j + 1) < n and p[j+1] == "*":
                memo[(i,j)] = (dfs(i,j+2) or (first and dfs(i+1,j)))
                return memo[(i,j)]
            if first:
                memo[(i,j)] =  dfs(i+1,j+1)
                return memo[(i,j)]
                
            memo[(i,j)] = False
            return memo[(i,j)]
        return dfs(0,0)