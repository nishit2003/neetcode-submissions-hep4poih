class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0 , len(nums) - 1
        while l <= r:
            m = l + ((r-l)//2)
            if nums[m] == target:
                return m
            
            if nums[m] >= nums[l]: #left side sorted
                if target > nums[m] or target < nums[l]:
                    # out of bounds in left sorted
                    l = m + 1
                else:
                    r = m - 1

            else:
                # right side sorted
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1



