class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        prereq = {i:[] for i in range(numCourses)}
        
        for pre in prerequisites:
            prereq[pre[0]].append(pre[1])
        print(prereq)

        
        visit = set()

        def dfs(node):
            if prereq[node] == []:
                return True
            
            if node in visit:
                return False

            visit.add(node)
            for each in prereq[node]:
                if not dfs(each):   
                    return False
                
            visit.remove(node)
            prereq[node] == []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True