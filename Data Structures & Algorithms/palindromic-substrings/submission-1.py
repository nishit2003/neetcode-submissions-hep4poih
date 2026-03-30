class Solution:
    def countSubstrings(self, s: str) -> int:
        # count = 0
        # n = len(s)
        # for i in range(n):
        #     for j in range(i,n):
        #         substr = s[i:j+1]

        #         if substr == substr[::-1]:
        #             count+=1

        # return count 

        count = 0

        for i in range(len(s)):
            # odd len
            l , r = i, i
            while l>=0 and r < len(s) and s[l] == s[r]:
                count +=1
                l-=1
                r+=1
            # even len
            l , r = i, i+1
            while l>=0 and r < len(s) and s[l] == s[r]:
                count +=1
                l-=1
                r+=1
        return count
