class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hashset = {i : [] for i in range(n)}
        for n1, n2 in edges:
            hashset[n1].append(n2)
            hashset[n2].append(n1)

        count = 0
        visit = set()

        def dfs(n1):
            if n1 in visit:
                return
            visit.add(n1)
            for neighbor in hashset[n1]:
                dfs(neighbor)
            
        for i in range(n):
            if i not in visit:
                count += 1
                dfs(i)

        return count
        