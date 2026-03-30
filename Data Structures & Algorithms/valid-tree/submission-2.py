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
        if self.rank[pv] > self.rank[pu]:
            self.parent[pu] = pv
            self.rank[pv]+=self.rank[pu]
        else:
            self.parent[pv] = pu
            self.rank[pu] += self.rank[pv]
        return True
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        dsu = DSU(n)
        for u,v in edges:
            if not dsu.union(u,v):
                return False
        return True