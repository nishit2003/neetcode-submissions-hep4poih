class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        valid = {i:[] for i in range(numCourses)}
        for pre, post in prerequisites:
            valid[pre].append(post)
        seen = set()

        def dfs(node):
            if valid[node] == []:
                return True
            if node in seen:
                return False
            seen.add(node)
            for each in valid[node]:
                if not dfs(each): return False
            seen.remove(node)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True