class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []

        def dfs(i):
            if i == len(nums):
                res.append(curr.copy())
                return 
            
            for x in nums:
                if x not in curr:
                    curr.append(x)
                    dfs(i+1)
                    curr.pop()
        
        dfs(0)
        return res