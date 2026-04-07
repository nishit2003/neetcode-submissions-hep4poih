class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        res = 0
        for ele in s:
            if ele in "()":
                if stack and stack[-1] == "(" and ele == ")":
                    stack.pop()
                else:
                    stack.append(ele)
                res = max(res,len(stack))
        return res