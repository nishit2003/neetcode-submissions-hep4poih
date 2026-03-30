class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        # count=0
        res = 0
        for n in nums:
            if n-1 not in numset:
                count=1
                while n+count in numset:
                    count+=1
                res = max(res,count)
        return res
        
