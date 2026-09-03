class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num,0)

        minheap = []
        for val,fre in freq.items():
            heapq.heappush(minheap,[fre,val])
            if len(minheap) > k:
                heapq.heappop(minheap)

        res = []
        while k:
            res.append(heapq.heappop(minheap)[1])
            k-=1
        return res