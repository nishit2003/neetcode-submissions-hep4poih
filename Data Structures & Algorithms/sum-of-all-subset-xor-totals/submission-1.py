class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        # res, curr = [], []
        # def dfs(i):
        #     if i >= len(nums):
        #         res.append(curr.copy())
        #         return 
            
        #     # to include
        #     curr.append(nums[i])
        #     dfs(i+1)
        #     curr.pop()

        #     # to not include
        #     dfs(i+1)
        
        # dfs(0)
        # total = 0
        # for i in res:
        #     xor = 0
        #     for ele in i:
        #         xor ^= ele
        #     total += xor
        
        # return (total)
        # # return res

        def dfs(i, total):
            if i == len(nums):
                return total
            
            # to include
            return dfs(i+1,total^nums[i]) + dfs(i+1,total)
            # not to include
        return dfs(0,0)