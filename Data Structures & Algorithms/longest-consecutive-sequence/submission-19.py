class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0
        cnt = 0
        for num in nums:
            if num-1 not in numset:
                cnt = 1
                while num + cnt in numset:
                    cnt +=1
            # else:
            #     numset.add(num) 
            res = max(res,cnt)
        return res