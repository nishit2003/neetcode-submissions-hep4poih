class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sol = []
        candidates = sorted(candidates)

        def bfs(i, total):
            if total == target:
                res.append(sol.copy())
                return 

            if i >= len(candidates) or total > target:
                return 

            

            # opt1 - to include
            sol.append(candidates[i])
            bfs(i+1, total + candidates[i])
            sol.pop()

            while i < len(candidates) - 1 and candidates[i] == candidates[i+1]:
                i+=1

            # opt2 - not to innlude
            bfs(i+1, total)

        bfs(0,0)
        return res