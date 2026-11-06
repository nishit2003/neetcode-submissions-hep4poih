class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1+ freq.get(num,0)
        
        maxheap = [[-cnt,val] for val,cnt in freq.items() ]
        heapq.heapify(maxheap)
        res = []

        while k:
            cnt,val = heapq.heappop(maxheap)
            res.append(val)
            k-=1

        return res
