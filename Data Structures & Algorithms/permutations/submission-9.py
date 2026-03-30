class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        curr = []
        res = []

        def backtrack(i):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return 
            
            for i in nums:
                if i not in curr:
                    curr.append(i)
                    backtrack(i+1)
                    curr.pop()

        backtrack(0)
        return res