from functools import lru_cache

class Solution:
    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        n = len(nums)

        @lru_cache(None)
        def dfs(l, r):
            if l + 1 == r:
                return 0

            res = 0
            for k in range(l + 1, r):
                coins = nums[l] * nums[k] * nums[r]
                coins += dfs(l, k) + dfs(k, r)
                res = max(res, coins)

            return res

        return dfs(0, n - 1)