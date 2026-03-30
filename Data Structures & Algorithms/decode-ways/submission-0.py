class Solution:
    def numDecodings(self, s: str) -> int:
        def helper(i):
            # count = 0
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0

            count = helper(i+1)

            if i+1 < len(s) and 1 < int(s[i:i+2]) <= 26:
                count+= helper(i+2)

            return count
        
        return helper(0)