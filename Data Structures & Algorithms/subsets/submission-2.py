class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []

        def backtracking(i):
            if i == len(nums):
                res.append(curr.copy())
                return

            # decision1 - to include
            curr.append(nums[i])
            backtracking(i+1)
            curr.pop()

            # decision2 - to not include
            backtracking(i+1)


        backtracking(0)
        return res