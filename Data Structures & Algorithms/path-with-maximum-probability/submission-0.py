class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {i:[] for i in range(n)}

        for i in range(len(edges)):
            adj[edges[i][0]].append((edges[i][1],succProb[i]))
            adj[edges[i][1]].append((edges[i][0], succProb[i]))


        maxH = [(-1,start_node)]
        seen = set()
        res = 0

        while maxH:
            prob1,node1 = heapq.heappop(maxH)
            if node1 in seen:
                continue
            seen.add(node1)

            if node1 == end_node:
                return -prob1
    
            
            for dst,prob2 in adj[node1]:
                if dst not in seen:
                    heapq.heappush(maxH,(prob1*prob2,dst))
        return 0