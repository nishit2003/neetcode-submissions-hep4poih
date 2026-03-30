class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i,a in enumerate(nums):
            if a == target:
                return i
            
        return -1