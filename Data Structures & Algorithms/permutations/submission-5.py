class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, cur = [], []

        def dfs(i):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            # if i > len(nums):
            #     return
            
            for x in nums:
                if x not in cur:
                    cur.append(x)
                    dfs(i)
                    cur.pop()
        dfs(0)
        return res