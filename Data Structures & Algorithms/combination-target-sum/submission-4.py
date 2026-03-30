class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []

        def backtrack(i):
            if  i == len(nums) or sum(curr) > target:
                return

            if target == sum(curr):
                res.append(curr.copy())
                return

            # case 1 - to include
            curr.append(nums[i])
            backtrack(i)
            curr.pop() # backtrack

            # case 2 - to not include
            backtrack(i+1)

        backtrack(0)
        return res