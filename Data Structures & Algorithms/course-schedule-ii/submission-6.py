class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}
        for pre in prerequisites:
            adj[pre[1]].append(pre[0])
        res = []
        visit = [0] * numCourses # 0 - unvisited, 1 - visiting, 2 - visited
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
            adj[node] == []
            res.append(node)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return res[::-1]         