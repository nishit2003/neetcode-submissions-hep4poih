class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num,0)

        minheap = []
        for val,fre in freq.items():
            minheap.append([-fre,val])
        heapq.heapify(minheap)

        res = []
        while k:
            fre, val = heapq.heappop(minheap)
            res.append(val)
            k-=1
        return res
