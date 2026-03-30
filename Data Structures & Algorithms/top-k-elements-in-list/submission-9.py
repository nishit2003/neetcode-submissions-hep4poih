class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num,0)

        maxHeap = []
        for val,cnt in freq.items():
            maxHeap.append([-cnt,val])
        heapq.heapify(maxHeap)
    
        res = []
        while k:
            cnt, val = heapq.heappop(maxHeap)
            res.append(val)
            k-=1
        
        return res


