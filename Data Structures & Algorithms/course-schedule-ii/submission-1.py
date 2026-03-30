class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        visit = set()
        res = []

        def dfs(crs):
            if crs in visit:
                return False
            if prereq[crs] == []:
                if crs not in res:
                    res.append(crs)
                return True
            visit.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre): return False
            visit.remove(crs)
            prereq[crs] = []
            res.append(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res