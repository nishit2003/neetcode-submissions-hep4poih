class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []

        def dfs(i):
            if len(nums) == len(curr):
                res.append(curr.copy())
                return
            
            if len(curr) > len(nums):
                return
            
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    dfs(i+1)
                
                    curr.pop()
            
        dfs(0)
        return res