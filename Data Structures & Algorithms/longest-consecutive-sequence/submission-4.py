class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for i in numset:
            if i-1 not in numset:
                count=1
            
                while (i+count) in numset:
                    count+=1

                longest = max(count, longest)

        return longest

            