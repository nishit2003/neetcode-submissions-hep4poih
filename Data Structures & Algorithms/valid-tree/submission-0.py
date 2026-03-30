class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # undirected graph
        childmap = {i : [] for i in range(n)}
        for par, ch in edges:
            childmap[par].append(ch)
            childmap[ch].append(par)

        visit = set()
    
        # recursive helper 
        def dfs(child, parent):
            if child in visit: #cycle
                return False
            
            visit.add(child)
            for neighbor in childmap[child]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, child):
                    return False
            return True

        return dfs(0, -1) and n == len(visit)

            