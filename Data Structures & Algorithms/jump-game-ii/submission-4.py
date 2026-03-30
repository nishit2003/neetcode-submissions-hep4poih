class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        curr = 0
        maxjump = 0

        for i in range(len(nums)-1):
            maxjump = max(maxjump,i+nums[i])
            if i == curr:
                curr = maxjump
                jumps+=1

        return jumps
