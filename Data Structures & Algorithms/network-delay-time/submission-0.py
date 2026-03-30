class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for u,v,w in times:
            if u not in adj:
                adj[u] = []
            adj[u].append([v,w])

        minheap = [(0,k)]
        visit = set()
        t = 0
        while minheap:
            w1,n1 = heapq.heappop(minheap)
            if n1 in visit:
                continue
            t = w1
            visit.add(n1)
            
            for n2,w2 in adj.get(n1,[]):
                if n2 not in visit:
                    heapq.heappush(minheap,(w1+w2,n2))
        return t if len(visit) == n else -1
                