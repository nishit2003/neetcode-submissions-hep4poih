class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:set() for i in range(numCourses)}
        for pre,post in prerequisites:
            adj[post].add(pre)
        visit = [0] * numCourses # 0 - Unvisited, 1 - visiting , 2 - visited 
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
        for c in range(numCourses):
            if not dfs(c):
                return []
        return res[::-1]