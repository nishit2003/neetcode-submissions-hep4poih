class Solution:
    def longestPalindrome(self, s: str) -> str:
        # res = ''
        # for i in range(len(s)):
        #     for j in range(i,len(s)):
        #         sub = s[i:j+1]
        #         if sub == sub[::-1]:
        #             if len(sub) > len(res):
        #                 res = sub
        # return res
        res = ''
        reslen = 0

        for i in range(len(s)):
            # odd len
            l,r = i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if len(s[l:r+1]) > reslen:
                    reslen = r-l+1
                    res = s[l:r+1]
                l-=1
                r+=1
            
            # even len
            l,r = i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if len(s[l:r+1]) > reslen:
                    reslen = r-l+1
                    res = s[l:r+1]
                l-=1
                r+=1
        return res