class DSU:
    def __init__(self,n) -> None:
        self.rank = [0] * n
        self.parent = list(range(n))

    def find(self,x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,u,v):
        pu,pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        
        elif self.rank[pu] > self.rank[pv]:
            self.rank[pu] += self.rank[pv]
            self.parent[pv] = pu
        else:
            self.rank[pv] += self.rank[pu]
            self.parent[pu] = pv
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        dsu = DSU(n)
        res = n
        for u,v in edges:
            if dsu.union(u,v):
                res -=1
        return res




