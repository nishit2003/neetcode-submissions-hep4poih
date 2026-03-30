class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        candidates.sort()
        def backtrack(start,total):
            if total == target:
                    res.append(curr.copy())
                    return
            for i in range(start, len(candidates)):
                
                if total > target or i == len(candidates):
                    return
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                curr.append(candidates[i])
                backtrack(i+1,total+candidates[i])
                curr.pop()


        backtrack(0,0)
        return res