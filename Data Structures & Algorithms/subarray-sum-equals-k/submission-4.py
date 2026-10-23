class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        data = {0:1}
        res = cur = 0

        for num in nums:
            cur += num
            diff = cur - k

            res += data.get(diff,0)
            data[cur] = 1 + data.get(cur,0)
        
        return res