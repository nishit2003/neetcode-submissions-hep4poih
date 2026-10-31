class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        
        maxH = [[-cnt,val] for val, cnt in freq.items()] 
        heapq.heapify(maxH)
        res = []
        while k:
            cnt,val = heapq.heappop(maxH)
            res.append(val)
            k-=1
        return res
