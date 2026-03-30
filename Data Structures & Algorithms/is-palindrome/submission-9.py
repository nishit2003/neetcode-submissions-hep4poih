class Solution:
    def isPalindrome(self, s: str) -> bool:
        # l, r = 0 , len(s) - 1

        # while l < r:
        #     if s[l] != s[r]:
        #         return False

        # return True

        res = ''
        for i in s:
            if self.alphanum(i):
                res+= i.lower()


        return res == res[::-1]

    def alphanum(self,x):
        if (ord('A') <= ord(x) <= ord('Z') or 
            (ord('a') <= ord(x) <= ord('z')) or             
            (ord('0') <= ord(x) <= ord("9") )):
            return True

        else:
            return False

