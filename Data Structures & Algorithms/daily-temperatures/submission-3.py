class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack= []

        # for i in range(len(temperatures)):
        #     for j in range(i+1,len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             result[i] = j - i
        #             break

        # return result

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                stackIdx, stackval = stack.pop()
                result[stackIdx] = i - stackIdx

            stack.append((i,t))

        return result


