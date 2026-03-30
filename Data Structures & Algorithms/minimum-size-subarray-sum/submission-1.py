class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
            res = float('inf')
            l = 0
            currsum = 0
            
            for r in range(len(nums)):
                # 1. Add the current number to our running total
                currsum += nums[r]
                
                # 2. While the sum is big enough, try to shrink from the left
                while currsum >= target:
                    res = min(res, r - l + 1) # Update the smallest length found
                    currsum -= nums[l]        # Subtract the 'old' left number
                    l += 1                    # Move the left wall in
                    
            # If res is still infinity, we never found a valid subarray
            return res if res != float('inf') else 0