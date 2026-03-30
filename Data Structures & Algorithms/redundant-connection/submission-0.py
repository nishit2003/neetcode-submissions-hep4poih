class DSU:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self,x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,u,v):
        pu,pv = self.find(u),self.find(v)
        if pu == pv:
            return False
        if self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
            self.rank[pu] += self.rank[pv]
        else:
            self.parent[pu] = pv
            self.rank[pv] += self.rank[pu]
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges)+1)
        for u,v in edges:
            if not dsu.union(u,v):
                return [u,v]