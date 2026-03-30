class Solution:
    def isPalindrome(self, s: str) -> bool:
       
        res = ''
        for i in s:
            if self.Alnum(i):
                res+=i.lower()

        return res == res[::-1]

    def Alnum(self, c):
        return (
            (ord('A') <= ord(c) <= ord('Z')) or
            (ord('a') <= ord(c) <= ord('z')) or
            (ord('0') <= ord(c) <= ord('9'))
            )