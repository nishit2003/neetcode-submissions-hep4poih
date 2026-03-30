class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []

        def backtrack(i):
            if i == len(nums):
                res.append(curr.copy())
                return 
            #case 2 - to not include
            backtrack(i+1)
            # case 1 - to include
            curr.append(nums[i])
            backtrack(i+1)
            curr.pop() # backtrack

            
        backtrack(0)
        return res