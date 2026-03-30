class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            if (n-1) not in numSet:
                current = 1

                while (n+current) in numSet:
                    current +=1

                longest = max(current, longest)
        
        return longest

