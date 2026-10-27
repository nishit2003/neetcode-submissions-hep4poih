class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        curr = []
        res = []
        nums.sort()

        def backtrack(i):
            if sum(curr) == target:
                res.append(curr.copy())
                return
            
            if i >= len(nums) or sum(curr) > target:
                return 

            curr.append(nums[i])
            backtrack(i)

            curr.pop()

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            
            backtrack(i+1)
        
        backtrack(0)
    
        return res