class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = {}
        for ch in s:
            freq[ch] = 1 + freq.get(ch,0)
        
        maxheap = []
        for ele, cnt in freq.items():
            maxheap.append([-cnt,ele])
        heapq.heapify(maxheap)

        prev = None
        res = ''
        while maxheap or prev:
            if not maxheap and prev:
                return ''
            frq,val = heapq.heappop(maxheap)
            res += val
            frq +=1
        
            if prev:
                heapq.heappush(maxheap,prev)
                prev = None
            
            if frq:
                prev = [frq,val]
        return res
