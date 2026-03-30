class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    
        memo = {}
        def dfs(s1,s2,i1,i2):
            if i1 == len(s1) or i2 == len(s2):
                return 0
            if (s1,s2,i1,i2) in memo:
                return memo[(s1,s2,i1,i2)]
            if s1[i1] == s2[i2]:
                memo[(s1,s2,i1,i2)] = 1 + dfs(s1,s2,i1+1,i2+1)
            else:
                memo[(s1,s2,i1,i2)] = max(dfs(s1,s2,i1+1,i2), dfs(s1,s2,i1,i2+1))
            return memo[(s1,s2,i1,i2)]
        return dfs(text1,text2,0,0)