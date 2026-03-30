class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0] * (len(nums))

        prefix[0] = nums[0]
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] + nums[i]
        print(prefix)

        currsum = prefix[-1]
        for i in range(len(prefix)):
            if currsum - prefix[i]==prefix[i]- nums[i]:
                return i
        return -1