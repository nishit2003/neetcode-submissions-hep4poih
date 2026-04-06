class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        

        check = [True] * n
        check[0] = check[1] = False
    
        for num in range(2,int(n ** 0.5)+1):
            if check[num]:
                for multiple in range(num * num,n,num):
                    check[multiple] = False
        return sum(check)
