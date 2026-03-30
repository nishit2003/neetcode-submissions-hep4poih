class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}
        def dfs(i,total):
            if (i,total) in memo:
                return memo[(i,total)]

            if total == amount:
                return 0
            if total > amount or i >= len(coins):
                return float('inf')
            
            # to skip
            skip = dfs(i+1, total)
            
            # to include
            inc = float('inf')
            if total + coins[i] <= amount:
                inc = min(inc,1+ dfs(i,total+coins[i]))
            
            memo[(i,total)] = min(skip,inc)

            return memo[(i,total)]
        
        resF = dfs(0,0)
        return resF if resF != float('inf') else -1