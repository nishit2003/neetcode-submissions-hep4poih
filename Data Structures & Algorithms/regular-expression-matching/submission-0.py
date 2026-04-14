class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        m,n = len(s), len(p)
        def dfs(i,j):
            if j == n:
                return i == m
            if i > m or j > n:
                return False

            first = i < m and (s[i]==p[j] or p[j] == ".")
            if (j + 1) < n and p[j+1] == "*":
                return (dfs(i,j+2) or (first and dfs(i+1,j)))
            
            if first:
                return dfs(i+1,j+1)
            return False
            
        return dfs(0,0)