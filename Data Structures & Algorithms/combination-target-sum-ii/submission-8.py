class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        curr = []

        def backtrack(i):
            if sum(curr) == target:
                res.append(curr.copy()) 
                return
            if sum(curr) > target or i >= len(candidates):
                return

            # to include
            curr.append(candidates[i])
            backtrack(i+1)
            curr.pop()

            # to not include
            j = i
            while j+1 < len(candidates) and candidates[j] == candidates[j+1]:
                j = j + 1

            backtrack(j+1)

        backtrack(0)
        return res
        