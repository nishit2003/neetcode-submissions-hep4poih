class Solution:
    def isValid(self, s: str) -> bool:
        valid = {'}':'{', ')': '(', ']':'['}
        stack = []

        for i in s:
            if i not in valid:
                stack.append(i)
                
            else:
                if stack and stack[-1] == valid[i]:
                    stack.pop()
                else:
                    return False
                
        
        return not stack