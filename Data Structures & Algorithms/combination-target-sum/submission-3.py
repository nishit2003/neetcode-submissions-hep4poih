class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr,total):
            # base case 1 when total is reached
            if total == target:
                res.append(curr.copy())
                return

            # base case 2 OOB, exceed total
            if i >= len(nums) or total > target:
                return

            # decision 1 to include
            curr.append(nums[i])
            dfs(i, curr , total + nums[i])
            curr.pop()

            # decision 2 to not include
            dfs(i+1,curr,total)

        dfs(0, [], 0)
        return res