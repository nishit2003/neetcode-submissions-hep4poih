class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def dfs(i):
            if i >= len(prices):
                return 0
            
            best = dfs(i+1)
            for a in range(i, len(prices)):
                if prices[i] < prices[a]:
                    # current profit + best future profit after cooldown
                    best = max(best, (prices[a] - prices[i]) + dfs(a + 2))
            
            return best

        return dfs(0)
        