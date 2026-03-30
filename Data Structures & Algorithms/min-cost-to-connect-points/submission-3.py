class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        size = len(points)
        adj = {i:[] for i in range(size)}
        for i in range(size):
            x1,y1 = points[i]
            for j in range(i+1,size):
                x2,y2 = points[j]
                dist = abs(x2-x1) + abs(y2-y1)
                adj[i].append((dist,j))
                adj[j].append((dist,i))

        minH = [(0,0)]
        seen = set()
        res = 0

        while minH:
            cost, node = heapq.heappop(minH)
            if node in seen:
                continue
            seen.add(node)

            res += cost
            for cost2,node2 in adj[node]:
                if node2 not in seen:
                    heapq.heappush(minH,(cost2,node2))
        return res