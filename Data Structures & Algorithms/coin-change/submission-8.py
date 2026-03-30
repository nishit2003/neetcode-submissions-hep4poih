class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}

        def dfs(i, total):
            if (i, total) in memo:
                return memo[(i, total)]

            if total == amount:
                return 0
            if total > amount or i == len(coins):
                return float('inf')

            # choice: skip or take
            skip = dfs(i + 1, total)
            take = 1 + dfs(i, total + coins[i])

            memo[(i, total)] = min(skip, take)
            return memo[(i, total)]

        res = dfs(0, 0)
        return res if res != float('inf') else -1