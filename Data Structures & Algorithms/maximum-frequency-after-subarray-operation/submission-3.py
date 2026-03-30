class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        cntK = 0
        for num in nums:
            if num == k:
                cntK+=1
        res = 0
        for i in range(1,51):
            curr = 0
            for num in nums:
                if num == i:
                    curr+=1
                if num == k:
                    curr-=1
                
                curr = max(0,curr)
                res = max(res,curr+cntK)

        return res