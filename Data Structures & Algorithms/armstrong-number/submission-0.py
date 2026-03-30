class Solution:
    def isArmstrong(self, n: int) -> bool:
        cnt= 0
        temp = n
        while temp > 0:
            cnt += 1
            temp = temp//10

        temp2 = n
        res = 0
        while temp2 > 0:
            char = temp2 % 10
            res += char ** cnt
            temp2 = temp2//10
        print(res)
        return res == n
        
            

            