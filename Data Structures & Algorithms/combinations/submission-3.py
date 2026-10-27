class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        

        res = []
        curr = []
        nums = list(range(1,n+1))
        print(nums)

        def backtrack(i):
            if len(curr) == k:
                res.append(curr.copy())
                return
            if i >= len(nums):
                return 
            
            curr.append(nums[i])
            backtrack(i+1)
        
            curr.pop()

            backtrack(i+1)
        backtrack(0)
        return res
