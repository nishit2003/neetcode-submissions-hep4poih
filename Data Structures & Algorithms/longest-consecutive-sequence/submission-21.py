class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        res = cnt = 0
        numset = set(nums)
        for num in nums:
            if num -1 not in numset:
                cnt = 1
                while num + cnt in numset:
                    cnt +=1
            res = max(res,cnt)
        
        return res