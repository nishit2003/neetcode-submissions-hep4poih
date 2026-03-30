class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def bfs(i, subset):
            if i == len(nums):
                res.append(subset.copy())
                return

            # option 1 to choose 
            subset.append(nums[i])
            bfs(i+1 , subset)
            subset.pop()

            # option 2 to not to choose

            bfs(i+1, subset)

        bfs(0,[])
        return res