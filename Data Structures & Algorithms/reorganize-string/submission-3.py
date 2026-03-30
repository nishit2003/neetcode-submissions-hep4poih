class Solution:
    def reorganizeString(self, s: str) -> str:
        res = ""
        freq = {}
        for ch in s:
            freq[ch] = 1 + freq.get(ch,0)
        
        maxheap = []
        for val,cnt in freq.items():
            maxheap.append([-cnt,val])
        heapq.heapify(maxheap)

        prev = None
        while maxheap or prev:
            if not maxheap and prev:
                return ""
            cnt, val = heapq.heappop(maxheap)
            cnt += 1
            res += val

            if prev:
                heapq.heappush(maxheap,prev)
                prev = None
            
            if cnt:
                prev = [cnt, val]
        
        return res
