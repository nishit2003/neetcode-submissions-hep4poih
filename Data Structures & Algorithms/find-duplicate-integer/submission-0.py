class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        values = defaultdict(int)
        for n in nums:
            values[n]+=1

        for val in values:
            if values[val] >1:
                return val