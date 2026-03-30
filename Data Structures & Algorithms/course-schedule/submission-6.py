class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = { i: [] for i in range(numCourses)}
        for pre, post in prerequisites:
            premap[pre].append(post)
        visit = set()

        def dfs(node):
            if node in visit:
                return False
            if premap[node] == []:
                return True
            visit.add(node)
            for pre in premap[node]:
                if not dfs(pre): return False
            visit.remove(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
