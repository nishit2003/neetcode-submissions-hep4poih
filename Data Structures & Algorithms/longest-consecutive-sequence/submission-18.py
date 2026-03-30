class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        cnt = 0
        for num in nums:
            if num - 1 not in nums:
                cnt = 1  
                while num + cnt in nums:
                    cnt +=1
            res = max(res,cnt)
        
        return res


# [1,2,4]
# [1,3,5,7,10]

# []1,2,3,4,5,6,7,8,9