class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        math = ["+","-","*","/"]

        stack = []
        for token in tokens:
            if token not in math:
                stack.append(int(token))

            else:
                a = stack.pop()
                b = stack.pop()

                if token == "+":
                    stack.append(a+b)

                if token == "-":
                    stack.append(b-a)
                    
                if token == "*":
                    stack.append(a*b)

                if token == "/":
                    stack.append(int(b/a))
        return stack[-1]