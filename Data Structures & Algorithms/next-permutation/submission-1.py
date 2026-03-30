class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find pivot
        n = len(nums)
        pivot = 0
        for i in range(n-1,0,-1):
            if nums[i] > nums[i-1]:
                pivot = i-1
                break
        if pivot == 0:
            return nums.sort()
        
        # swap the elements
        for i in range(n-1,pivot,-1):
            if nums[i] > nums[pivot]:
                nums[pivot],nums[i] = nums[i], nums[pivot]
                break
        
        # sort the second half
        nums[pivot+1:] = reversed(nums[pivot+1:])

