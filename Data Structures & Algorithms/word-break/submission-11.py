class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set(wordDict)
        memo = {}
        def dfs(sub):
            if sub in memo:
                return memo[sub]
            if not sub:
                return True
            for i in range(1,len(sub)+1):
                prefix = sub[:i]
                if prefix in wordset:
                    suffix = sub[i:]
                    if dfs(suffix):
                        memo[sub] = True
                        return True
            
            memo[sub] = False
            return memo[sub]
        
        return dfs(s)
