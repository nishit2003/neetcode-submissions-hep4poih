class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        data = {i:[] for i in range(n)}
        for pre,post in edges:
            data[pre].append(post)
            data[post].append(pre)
        print(data)
        visit = set()

        def dfs(node):
            if node in visit:
                return False

            visit.add(node)
            for each in data[node]:
                dfs(each)
                
            # visit.remove(node)
            # return True

        cycle = 0
        for i in range(n):
            if i not in visit:
                cycle +=1
                dfs(i)
        return cycle