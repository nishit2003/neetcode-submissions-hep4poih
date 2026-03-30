class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []

        def backtrack(i):
            if i == len(nums):
                res.append(curr.copy())
                return
            
            if i > len(nums):
                return
            
            # to use
            curr.append(nums[i])
            backtrack(i+1)
            curr.pop()

            # to not use
            backtrack(i+1)

        backtrack(0)
        return res