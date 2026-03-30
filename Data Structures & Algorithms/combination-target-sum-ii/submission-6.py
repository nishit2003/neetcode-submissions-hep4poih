class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, curr = [], []
        candidates.sort()
        def dfs(idx,total):
            if total == target:
                res.append(curr.copy())
                return 
            if idx >= len(candidates) or total > target:
                return 

            for i in range(idx,len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                curr.append(candidates[i])
                dfs(i+1,total+candidates[i])
                curr.pop()

        dfs(0,0)
        return res
            
            