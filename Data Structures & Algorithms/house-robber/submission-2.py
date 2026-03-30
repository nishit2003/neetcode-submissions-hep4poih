from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob1, rob2, n , n + 1


        @lru_cache(None)
        def dfs(i):
            if i >= len(nums):
                return 0
            
            return max(dfs(i+1),nums[i]+dfs(i+2))
        return dfs(0)
    