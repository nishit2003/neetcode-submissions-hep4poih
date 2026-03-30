class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-stone for stone in stones]
        heapq.heapify(maxheap)

        while len(maxheap) > 1:
            a = heapq.heappop(maxheap)
            b = heapq.heappop(maxheap)

            if b > a:
                val = a - b
                heapq.heappush(maxheap,val)
        heapq.heappush(maxheap,0)
        return abs(maxheap[0])

        