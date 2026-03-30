class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        n = len(s)

        for i in range(n):
            for j in range(i,n):
                substr = s[i:j+1]

                if substr == substr[::-1]:
                    if len(substr) > len(longest):
                        longest = substr


        return longest