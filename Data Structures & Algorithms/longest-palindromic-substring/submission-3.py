class Solution:
    def longestPalindrome(self, s: str) -> str:
        # naive way
        longest = ''
        for i in range(len(s)):
            for j in range(i,len(s)):
                substr = s[i:j+1]

                if substr == substr[::-1]:
                    if len(substr)> len(longest):
                        longest = substr

        return longest