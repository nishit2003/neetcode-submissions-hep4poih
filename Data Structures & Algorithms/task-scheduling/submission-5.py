class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time =0
        freq = {}
        for task in tasks:
            freq[task] = 1 + freq.get(task,0)
        
        maxheap = []
        for task,cnt in freq.items():
            maxheap.append(-cnt)
        heapq.heapify(maxheap)

        deq = deque()

        while maxheap or deq:
            time +=1
            if maxheap:
                temp = 1 + heapq.heappop(maxheap)
                if temp:
                    deq.append((time+n,temp))
            if deq and deq[0][0] == time:
                heapq.heappush(maxheap,deq.popleft()[1])
        return time