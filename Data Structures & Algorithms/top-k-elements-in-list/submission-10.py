class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = 1 + freq.get(n,0)
        
        minheap = []
        for val,fre in freq.items():
            minheap.append([-fre,val])
        heapq.heapify(minheap)

        res = []
        while k:
            freq,val = heapq.heappop(minheap)
            res.append(val)
            k-=1
        return res

        print(minheap)