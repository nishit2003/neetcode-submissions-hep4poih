class DSU:
    def __init__(self,n):
        self.parent = [i for i in range(n)] # every element is parent of its own
        self.rank = [1] * n # all eles have same rank 1
    
    def find(self,node):
        curr = node
        while curr != self.parent[curr]:
            self.parent[curr] = self.parent[self.parent[curr]] #path compression
            curr = self.parent[curr]# going up the tree
        return curr
    
    def union(self,u,v):
        pu,pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
            self.rank[pu] += self.rank[pv]
        else:
            self.parent[pu] = pv
            self.rank[pv] += self.rank[pu]       
        return 1 
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = n
        dsu = DSU(n)
        for i,v in edges:
            if dsu.union(i,v):
                res-=1
        return res
        