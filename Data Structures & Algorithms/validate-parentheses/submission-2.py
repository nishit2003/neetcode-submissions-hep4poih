class Solution:
    def isValid(self, s: str) -> bool:
        valid = {')':'(', '}':'{', ']':'['}
        stack = []

        for i in s:
            if i in valid: #clsoing
                if stack and stack[-1] == valid[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return not stack

        