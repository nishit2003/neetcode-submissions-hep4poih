class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = -1

        # find smallest ele from right(pivot)
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                pivot = i
                break
        
        if pivot == -1:
            return nums.sort()

        # find the first elem greater than the pivot and swap
        for i in range(len(nums)-1,pivot,-1):
            if nums[i] > nums[pivot]:
                nums[i],nums[pivot] = nums[pivot],nums[i]
                break

        # sort the second half
        nums[pivot+1:] = reversed(nums[pivot+1:])
        