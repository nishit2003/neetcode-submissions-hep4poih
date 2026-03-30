class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {")":"(","]":"[","}":"{"}

        # if len(s)/2 != 0:
        #     return False

        for ele in s:
            if ele in valid:
                if not stack or stack.pop() != valid[ele]:
                    return False
            else:
                stack.append(ele)

        return not stack

            