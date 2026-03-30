class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res, curr = [],[]
        candidates.sort()

        def dfs(i,total):
            if total == target:
                res.append(curr.copy())
                return
            if i>=len(candidates) or total > target:
                return
            

            for j in range(i,len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
            
                # to include
                curr.append(candidates[j])
                dfs(j+1,total+candidates[j])

                # to not include
                curr.pop()
            # dfs(i+1,total)
        dfs(0,0)
        return res