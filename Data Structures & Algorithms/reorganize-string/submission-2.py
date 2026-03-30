class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = {}
        res = ''
        for i in s:
            freq[i] = 1 + freq.get(i,0)
        
        maxheap = []
        for val,cnt in freq.items():
            maxheap.append([-cnt,val])
        print(maxheap)
        heapq.heapify(maxheap)
        print(maxheap)

        prev = None
        while maxheap or prev:
            if not maxheap and prev:
                return ""

            cnt,val = heapq.heappop(maxheap)
            res += val
            cnt += 1

            if prev:
                heapq.heappush(maxheap,prev)
                prev = None
            
            if cnt!=0:
                prev = [cnt, val]

        return res
