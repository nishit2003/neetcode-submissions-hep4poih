class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        values = {'}':'{', ']':'[', ')':'('}

        for i in s:
            if i in values:
                topElem = stack.pop() if stack else False

                if values[i] != topElem:
                    return False

            else:
                stack.append(i)

        return not stack