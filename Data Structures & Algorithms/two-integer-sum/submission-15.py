class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}

        for idx,val in enumerate(nums):
            compliment = target - val
            if compliment in values:
                return [values[compliment],idx]
            
            values[val] = idx