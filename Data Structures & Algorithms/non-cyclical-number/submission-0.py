class Solution:
    def isHappy(self, n: int) -> bool:
        slow , fast = n , self.helper(n)
        
        while slow != fast:
            fast = self.helper(fast)
            fast = self.helper(fast)
            slow = self.helper(slow)

        return True if fast == 1 else False


    def helper(self, n):
        res = 0
        while n:
            res += (n % 10) ** 2
            n = n //10

        return res