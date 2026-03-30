class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, curr = [],[]
        
        def dfs(i):
            if sum(curr) == target:
                res.append(curr.copy())
                return
            
            if i >= len(nums) or sum(curr) > target:
                return
            
            # to include
            curr.append(nums[i])
            dfs(i)
            curr.pop()

            # to not include
            dfs(i+1)

        dfs(0)
        return res