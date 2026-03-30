class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 0
        numset = set(nums)

        for i in numset:
            if (i-1) not in numset:
                count = 1

                while (i + count) in numset:
                    count += 1
                length = max(count, length)
        return length