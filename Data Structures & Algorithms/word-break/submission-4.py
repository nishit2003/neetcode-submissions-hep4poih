class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        memo = {}

        def helper(sub):
            if not sub:
                return True
            
            if sub in memo:
                return memo[sub]

            for i in range(1,len(sub)+1):
                prefix = sub[:i]

                if prefix in wordSet:
                    if helper(sub[i:]):
                        memo[sub] = True  
                        return True
            memo[sub] = False  
            return False

        return helper(s)