class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num,0)
        res = []

        for key in freq:
            if freq[key] > len(nums) //2:
                res.append(key)
        return res[0]