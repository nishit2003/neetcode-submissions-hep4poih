class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''
        for i in s:
            if (i.isalnum() == True):
                res +=i.lower()

        return res[::-1] == res
