class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, curr = [],[]

        def backtrack(i):
            if i == len(nums):
                res.append(curr.copy())
                return
            
            if i >= len(nums):
                return
            
            # to include
            curr.append(nums[i])
            backtrack(i+1)
            curr.pop()

            # to not include
            j = i
            while j+1 < len(nums) and nums[j] == nums[j+1]:
                j=j+1
            backtrack(j+1)
        backtrack(0)
        return res