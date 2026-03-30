class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        freq = {}
        for n in nums:
            freq[n] = 1 + freq.get(n,0)

        def dfs(i):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for n in freq:
                if freq[n] > 0:
                    freq[n] -= 1
                    curr.append(n)
                
                    dfs(i)

                    freq[n] += 1
                    curr.pop()
        dfs(0)
        return res