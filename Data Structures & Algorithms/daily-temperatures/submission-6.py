class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for idx,val in enumerate(temperatures):
            while stack and val > stack[-1][1]:
                Oidx,Oval = stack.pop()
                res[Oidx] = idx-Oidx
            stack.append((idx,val))
        return res
