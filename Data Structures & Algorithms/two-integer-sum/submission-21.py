class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = {}

        for i,val in enumerate(nums):
            diff = target - val
            if diff in data:
                return [data[diff],i]
            
            data[val] = i