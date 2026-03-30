class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr=set()
        for i in nums:
            if i in arr:
                return True
            else:
                arr.add(i)
        return False
                
