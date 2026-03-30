class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        char = set(nums)
        res = 0
        for num in char:
            if num - 1 not in char:
                cnt = 1
                while num + cnt in char:
                    cnt+=1
                res = max(res, cnt)
        return res
                 