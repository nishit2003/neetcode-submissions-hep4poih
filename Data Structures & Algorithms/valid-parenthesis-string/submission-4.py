class Solution:
    def checkValidString(self, s: str) -> bool:
        # cache = {}
        # def dfs(i,open):
        #     if open < 0:
        #         return False
        #     key = (i,open)
        #     if key in cache:
        #         return cache[key]
        #     if i == len(s):
        #         return open == 0
        #     if s[i] == "(":
        #         res = dfs(i+1,open+1)
        #     elif s[i] == ")":
        #         res = dfs(i+1,open-1)
        #     else:
        #         res = (
        #         (dfs(i+1,open)) or
        #         (dfs(i+1,open+1)) or
        #         (dfs(i+1,open-1)))

        #     cache[key] = res
        #     return res
        # return dfs(0,0)

        leftmin, leftmax = 0,0
        for c in s:
            if c == '(':
                leftmin, leftmax = leftmin + 1, leftmax + 1
            elif c == ')':
                leftmin, leftmax = leftmin - 1, leftmax - 1
            else:
                leftmin, leftmax = leftmin - 1, leftmax + 1
            if leftmax < 0:
                return False
            if leftmin<0:
                leftmin = 0
        return leftmin == 0