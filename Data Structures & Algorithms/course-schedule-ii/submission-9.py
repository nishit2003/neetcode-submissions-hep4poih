class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            adj[pre].append(crs)
        visit = [0] * numCourses
        res = []
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
            res.append(node)
            return True
        
        res = []
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res[::-1]
