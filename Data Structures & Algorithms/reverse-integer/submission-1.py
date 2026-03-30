class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2**31
        MAX = 2**31 - 1

        res = 0
        while x:
            digit = int(math.fmod(x,10))
            x = int(x/10)

            res = (res*10) + digit

        if MIN <= res <= MAX:
            return res
        else:
            return 0