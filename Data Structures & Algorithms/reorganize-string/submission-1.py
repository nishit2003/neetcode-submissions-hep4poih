class Solution:
    def reorganizeString(self, s: str) -> str:
        values = {}
        res = ""
        for ele in s:
            values[ele] = 1 + values.get(ele,0)

        maxHeap = []
        for ele, cnt in values.items():
            maxHeap.append([-cnt,ele])
        heapq.heapify(maxHeap)    
        # print(maxHeap)
        
        prev = None
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
        
            cnt, val = heapq.heappop(maxHeap)
            res += val
            cnt += 1

            if prev:
                heapq.heappush(maxHeap,prev)
                prev = None

            if cnt !=0 :
                prev = [cnt,val]
            
        return res
