class UnionFind:
    def __init__(self, n: int):
        self.rank = [0] * n
        self.parent = list(range(n))
        self.comp = n

    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        px,py = self.find(x), self.find(y)
        return px == py

    def union(self, x: int, y: int) -> bool:
        px,py = self.find(x), self.find(y)
        if px == py:
            return False
        else:
            if self.rank[px] < self.rank[py]:
                self.rank[py] += self.rank[px]
                self.parent[px] = py
            else:
                self.rank[px] += self.rank[py]
                self.parent[py] = px
            self.comp -= 1
            return True
        
    def getNumComponents(self) -> int:
        return self.comp
