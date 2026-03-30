class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        cntK = 0
        for n in nums:
            if n == k:
                cntK += 1

        res = 0
        for i in range(1,51):
            cnt = 0
            for num in nums:
                if num == i:
                    cnt += 1
                if num == k:
                    cnt -= 1
                cnt = max(cnt,0)
                res = max(res,cntK+cnt)
        return res