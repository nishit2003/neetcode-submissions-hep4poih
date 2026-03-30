class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {']':'[', '}':'{', ')':'('}

        for i in s:
            # If it's an opening bracket, push onto the stack
            if i not in valid:
                stack.append(i)

            # If it's a closing bracket
            else:
                # Check if stack is not empty and the top matches
                if stack and stack[-1] == valid[i]:
                    stack.pop()
                else:
                    return False  # Stack is empty or top doesn't match
        
        # If stack is empty, it means all brackets are properly closed
        return not stack
            
                
                