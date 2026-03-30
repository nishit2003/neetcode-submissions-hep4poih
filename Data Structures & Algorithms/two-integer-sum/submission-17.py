class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        values = {}

        for idx,val in enumerate(nums):
            diff = target - val
            if diff in values:
                return [values[diff],idx]
            
            values[val] = idx