class Solution:
    def reverse(self, x: int) -> int:
        MinInt, MaxInt = -2**31,2**31-1
        # -2147483648
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0
        while x:
            digit = x%10
            x = x//10
            # pos check
            if res > MaxInt // 10 or (res == MaxInt//10 and digit > MaxInt % 10):
                return 0
            # neg check
            if res < MinInt // 10 or (res == MinInt//10 and digit < MinInt % 10):
                return 0
            res = res*10 + digit
        return sign*res 
