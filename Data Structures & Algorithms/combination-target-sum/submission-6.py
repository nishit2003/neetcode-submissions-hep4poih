class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res, curr = [],[]
        # def dfs(i):
        #     if sum(curr) == target:
        #         res.append(curr.copy())

        #     # to include
        #     curr.append(nums[i])
        #     dfs(i)
            
        #     # to not include
        #     curr.pop()
        #     dfs(i+1)

        # dfs(0)
        # return res

        def dfs(i,total):
            if total == target:
                res.append(curr.copy())
                return
            if i >=len(nums) or total > target:
                return
            
            # to including
            curr.append(nums[i])
            dfs(i,total + nums[i])

            # to not include
            curr.pop()
            dfs(i+1,total)
        dfs(0,0)
        return res
        