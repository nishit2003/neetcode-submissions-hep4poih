class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i:[] for i in range(n)}
        for s,d,w in flights:
            if s not in adj:
                adj[s] = []
            adj[s].append((d,w))
        seen = set()
        minheap = [(0,src,0)]
        while minheap:
            w1,n1,stps = heapq.heappop(minheap)
            if n1 == dst:
                return w1
            for nei in adj.get(n1,[]):
                neidst, neicost = nei[0],nei[1]
                if stps <= k:
                    heapq.heappush(minheap,(w1+neicost,neidst,stps+1))
        return -1
            
