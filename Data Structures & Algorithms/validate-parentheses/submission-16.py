class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        data = {"}":"{", ")":"(" , "]":"["}
        for b in s:
            if b in data: # closing bracket
                if not stack:
                    return False
                if stack and stack[-1] != data[b]:
                    return False
                stack.pop()
            else: # opening bracket
                stack.append(b)
        return not stack
    
# s = "(])"
# 
# stack = (