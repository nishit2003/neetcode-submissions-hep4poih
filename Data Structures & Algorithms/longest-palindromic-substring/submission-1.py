class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        # n = len(s)

        # for i in range(n):
        #     for j in range(i,n):
        #         substr = s[i:j+1]

        #         if substr == substr[::-1]:
        #             if len(substr) > len(longest):
        #                 longest = substr

        res = ""
        for i in range(len(s)):
            # odd len
            l,r = i,i
            while l >= 0 and r < len(s) and s[l]==s[r]:
                if r-l+1 > longest:
                    res = s[l:r+1]
                    longest = r-l+1
                l-=1
                r+=1


            # even len
            l,r = i,i+ 1
            while l >= 0 and r < len(s) and s[l]==s[r]:
                if r-l+1 > longest:
                    res = s[l:r+1]
                    longest = r-l+1
                l-=1
                r+=1
        return res