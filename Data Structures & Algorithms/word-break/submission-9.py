class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        memo = {}
        def helper(sub):
            if not sub:
                return True
            if sub in memo:
                return memo[sub]
            
            for i in range(1,len(sub)+1):
                prefix = sub[:i]
                if prefix in wordDict:
                    suffix = sub[i:]
                    if helper(suffix):
                        memo[sub] = True
                        return True
            else:
                memo[sub] = False
            return memo[sub]        
        return helper(s)