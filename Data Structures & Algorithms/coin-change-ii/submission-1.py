class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dfs(i,total):
            if (i,total) in memo:
                return memo[(i,total)]
            if total == amount:
                return 1
            
            if i >= len(coins) or total > amount:
                return 0
            
            # to skip
            skip = dfs(i+1,total)

            # to include
            inc = 0
            if total + coins[i] <= amount:
                inc = dfs(i,total+coins[i])

            memo[(i,total)] = skip + inc
            return memo[(i,total)]
        
        # res = dfs(0,0)
        return dfs(0,0)
