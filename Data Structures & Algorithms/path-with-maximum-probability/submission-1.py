class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {i: [] for i in range(n)}
        for edge,prob in zip(edges,succProb):
            adj[edge[0]].append([-prob,edge[1]])
            adj[edge[1]].append([-prob,edge[0]])
        
        visit = set()
        minheap = [(-1,start_node)]
        # res = 0.0
        while minheap:
            p1,n1 = heapq.heappop(minheap)
            if n1 in visit:
                continue
            # res = p1
            if n1 == end_node:
                return -p1
            
            visit.add(n1)
            for p2,n2 in adj.get(n1,[]):
                if n2 not in visit:
                    heapq.heappush(minheap, [-p1*p2,n2])
                

        return 0.0 
        
