class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        curr = []
        res = []

        def backtrack():
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for x in nums:
                if x not in curr:
                    curr.append(x)
                    backtrack()
                    curr.pop()

        backtrack()
        return res