class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            adj[crs].append(pre)
        visit = [0] * numCourses #0-unvisit, 1- visit, 2-visited

        def dfs(node):
            if visit[node] == 1:
                return False
            if visit[node] == 2:
                return True
            visit[node] = 1
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            visit[node] = 2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True