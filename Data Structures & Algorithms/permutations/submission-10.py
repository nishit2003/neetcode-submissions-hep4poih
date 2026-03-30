class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []

        def backtrack(i):
            if i == len(nums):
                res.append(curr.copy())
                return
            if i >= len(nums):
                return
            
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(i+1)
                    curr.pop()


        backtrack(0)
        return res
