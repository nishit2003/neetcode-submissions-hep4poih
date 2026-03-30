class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []

        def backtracking(i):
            while i == len(nums):
                res.append(sol.copy())
                return

            #we decide not to include
            backtracking(i+1)

            # we decide to include
            sol.append(nums[i])
            backtracking(i+1)
            sol.pop()

        backtracking(0)
        return res