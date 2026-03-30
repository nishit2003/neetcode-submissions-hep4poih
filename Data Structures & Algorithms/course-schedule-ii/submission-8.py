class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = {i: [] for i in range(numCourses)}
        for pre,post in prerequisites:
            adj[post].append(pre)
        res = []
        visit = [0] * numCourses #0- unvisited, 1- visiting, 2 - visited
        def dfs(i):
            if visit[i] == 1:
                return False
            if visit[i] == 2:
                return True
            
            visit[i] = 1
            for nei in adj[i]:
                if not dfs(nei):
                    return False
            visit[i] = 2
            res.append(i)
            return True
        
        for node in adj:
            if not dfs(node):
                return []
        return res[::-1]
