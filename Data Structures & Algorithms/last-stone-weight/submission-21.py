class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = []
        for each in stones:
            heapq.heappush(maxheap,-1*each)
        print(maxheap)

        while len(maxheap) > 1:
            a,b = heapq.heappop(maxheap) ,heapq.heappop(maxheap)
            if a!=b:
                heapq.heappush(maxheap,-1*abs(a-b))
            
        return -1*maxheap[0] if maxheap else 0
            