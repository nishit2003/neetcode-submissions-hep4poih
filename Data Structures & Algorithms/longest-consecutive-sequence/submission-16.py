class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        cnt = 0
        for n in nums:
            if n-1 not in nums:
                cnt = 1
                while n + cnt in nums:
                    cnt += 1
            res = max(res,cnt)
        
        return res
