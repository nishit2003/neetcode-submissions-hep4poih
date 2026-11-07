class DSU:
    def __init__(self,n) -> None:
        self.rank = [0] * n
        self.parent = list(range(n))
    
    def find(self,x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,u,v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False
        if self.rank[pu] > self.rank[pv]:
            self.rank[pu] += self.rank[pv]
            self.parent[pv] = pu
        else:
            self.rank[pv] += self.rank[pu]
            self.parent[pu] = pv

        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges)+1)
        for u,v in edges:
            if not dsu.union(u,v):
                return [u,v]
        