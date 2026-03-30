class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        maths = ['+','-','/','*']
        stack = []
        for token in tokens:
            if token not in maths:
                stack.append(token)

            else:
                b = int(stack.pop())
                a = int(stack.pop())

                if token == "+":
                    stack.append(b+a)

                if token == "*":
                    stack.append(b*a)
                
                if token =="-":
                    stack.append(a-b)

                if token == "/":
                    stack.append(int(a/b))

        return int(stack[-1])
                 