class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #pair here

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                StackT, StackInt = stack.pop()
                res[StackInt] = i - StackInt
            stack.append((t,i))
        return res