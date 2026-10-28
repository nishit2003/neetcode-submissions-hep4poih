class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[pre].append(crs)
        
        seen = set()
        res = []
        def dfs(node):
            if node in seen:
                return False

            # if adj[node] == []:
            #     return True

            seen.add(node)
            for nei in adj.get(node,[]):
                if not dfs(nei):
                    return False

            seen.remove(node)
            res.append(node)
            adj[node] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res[::-1]
