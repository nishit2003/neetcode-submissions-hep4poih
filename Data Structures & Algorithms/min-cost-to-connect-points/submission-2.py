class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        size = len(points)
        adj = {i:[] for i in range(size)}
        for i in range(size):
            x1,y1 = points[i]
            for j in range(i+1,size):
                x2,y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        
        res = 0
        minheap = [[0,0]]
        visit = set()
        while len(visit) < size:
            cost,i = heapq.heappop(minheap)
            if i in visit:
                continue
            visit.add(i)
            res+=cost
            for neicost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minheap,[neicost,nei])
        return res

