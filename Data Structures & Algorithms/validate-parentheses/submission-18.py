class Solution:
    def isValid(self, s: str) -> bool:
        data = {"]":"[" , "}": "{" , ")" : "("}
        stack = []

        for ele in s:
            if ele in data:
                if not stack:
                    return False
                
                if stack and stack[-1] != data[ele]:
                    return False

                stack.pop()

            else:
                stack.append(ele)
        
        return not stack