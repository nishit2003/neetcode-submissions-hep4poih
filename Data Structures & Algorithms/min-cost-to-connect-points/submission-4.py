class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i:[] for i in range(n)}
        for i in range(n):
            x1,y1 = points[i]
            for j in range(i+1,n):
                x2,y2 = points[j]
                dist = abs(x2-x1) + abs(y2-y1)
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        
        minheap = [[0,0]]
        visit = set()
        res = 0
        while minheap:
            cost, index = heapq.heappop(minheap)
            if index in visit:
                continue
            visit.add(index)
            res += cost
            for c2,i2 in adj.get(index,[]):
                if i2 not in visit:
                    heapq.heappush(minheap,[c2,i2])
        return res