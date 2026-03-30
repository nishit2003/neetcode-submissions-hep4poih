class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = { i: [] for i in range(numCourses)}
        for pre, post in prerequisites:
            premap[pre].append(post)
        visit = [0] * numCourses #0-unvisited, 1-visiting, 2 - visited

        def dfs(node):
            if visit[node] == 1:
                return False
            if premap[node] == [] or visit[node] == 2:
                return True
            visit[node] = 1
            for nei in premap[node]:
                if not dfs(nei): return False
            visit[node] = 2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
