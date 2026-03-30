class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        temp = []
        for i,v in enumerate(temperatures):
            while temp and v > temp[-1][1]:
                tempi, tempv = temp.pop()
                res[tempi] = i - tempi
            
            temp.append((i,v))
        return res

        # res = [0]*len(temperatures)
        # for i in range(len(temperatures)):
        #     for j in range(i,len(temperatures)):
        #         if temperatures[j]>temperatures[i]:
        #             res[i]= j-i
        #             break

        # return res