class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        nums.sort()
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
            j = i
            while j + 1 < len(nums) and nums[j] == nums[j+1]:
                j=j+1
            
            backtrack(j+1)
        backtrack(0)
        return res