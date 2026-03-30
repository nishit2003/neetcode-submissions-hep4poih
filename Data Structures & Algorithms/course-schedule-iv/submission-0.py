class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i:[] for i in range(numCourses)}
        for pre,post in prerequisites:
            if post not in adj:
                adj[post] = []
            adj[post].append(pre)

        def dfs(v,target,seen):
            if v == target:
                return True
            
            if v in seen:
                return False
            
            seen.add(v)
            for nei in adj[v]:
                if dfs(nei,target,seen):
                    return True
            return False
        
        res = []
        for u,v in queries:
            res.append(dfs(v,u,set()))
        return res