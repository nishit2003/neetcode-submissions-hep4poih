class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        data = {0:1}
        res = 0
        curr = 0
        for num in nums:
            curr+=num
            diff = curr - k

            res += data.get(diff,0)
            data[curr] = 1 + data.get(curr,0)
        return res