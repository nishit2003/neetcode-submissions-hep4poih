class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def dfs(amount):
            if amount <= 0:
                return 0
            if amount in dp:
                return dp[amount]
            
            res = float('inf')
            for coin in coins:
                if amount - coin >= 0:
                    dp[amount] = res = min(res,1+dfs(amount-coin))
            return res
        mincoin = dfs(amount)
        return dfs(amount) if mincoin != float('inf') else -1