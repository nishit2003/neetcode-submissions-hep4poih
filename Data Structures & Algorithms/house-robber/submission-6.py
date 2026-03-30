class Solution:
    def rob(self, nums: List[int]) -> int:
    #    DP - TOP DOWN
        # memo = {}

        # def dfs(i):
        #     if i >= len(nums):
        #         return 0
        #     if i in memo:
        #         return memo[i]
        #     memo[i] =  max(dfs(i+1),nums[i]+dfs(i+2))
        #     return memo[i]
        # return dfs(0)
    

         # rob1, rob2, n , n + 1

        #  ITERATIVE - DP

        rob1, rob2 = 0 , 0
        for n in nums:
            temp = max(n+rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2