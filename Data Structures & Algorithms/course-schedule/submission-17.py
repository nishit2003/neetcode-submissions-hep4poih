class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i : [] for i in range(numCourses)}
        for u,v in prerequisites:
            adj[v].append(u)

        seen = set()
        safe = set()

        def dfs(node):
            if node in seen:
                return False # cycle detected
            if adj[node] == []:
                return True
            seen.add(node)

            for nei in adj.get(node,[]):
                if not dfs(nei):
                    return False
            
            seen.remove(node)
            # safe.add(node)
            adj[node] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True