class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            if prereq[crs] == []:
                return True
            visit.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre): return False
            visit.remove(crs)
            prereq[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c): 
                return False
        return True
