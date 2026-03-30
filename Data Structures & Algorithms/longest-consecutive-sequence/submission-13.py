class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        cnt = 0
        res = 0
        for n in nums:
            if n-1 not in numset:
                cnt = 1
                while n+cnt in numset:
                    cnt += 1
                res = max(res,cnt)

        return res