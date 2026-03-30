from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        memo = {}  # Dictionary to store results for substrings
        
        def helper(sub: str) -> bool:
            # Base case: if the substring is empty, we've successfully segmented the string.
            if not sub:
                return True

            # Return the cached result if we have computed this substring before.
            if sub in memo:
                return memo[sub]
            
            # Try every possible split for the substring.
            for i in range(1, len(sub) + 1):
                prefix = sub[:i]
                # If the prefix is a valid word...
                if prefix in wordSet:
                    # Recursively check if the remainder of the string can be segmented.
                    if helper(sub[i:]):
                        memo[sub] = True  # Cache the result for this substring.
                        return True

            memo[sub] = False  # Cache the result before returning.
            return False

        return helper(s)
