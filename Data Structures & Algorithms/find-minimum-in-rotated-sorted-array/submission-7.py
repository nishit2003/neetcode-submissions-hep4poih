class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        curr_min = float('inf')  # Initialize curr_min to a very large number

        while l <= r:
            m = (l + r) // 2
            curr_min = min(curr_min, nums[m])  # Update curr_min with the smallest value seen
            
            if nums[m] > nums[r]:
                # The minimum is in the right part
                l = m + 1
            else:
                # The minimum is in the left part or at mid
                r = m - 1

        return curr_min
