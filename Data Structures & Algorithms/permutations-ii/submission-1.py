class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        cnt = {}
        for num in nums:
            cnt[num] = 1 + cnt.get(num,0)

        def backtrack(i):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            if len(curr) > len(nums):
                return
            
            for key in cnt:
                if cnt[key] > 0:
                    curr.append(key)
                    cnt[key] -= 1

                    backtrack(i+1)

                    cnt[key] += 1
                    curr.pop()
        backtrack(0)
        return res