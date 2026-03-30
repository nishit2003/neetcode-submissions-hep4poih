class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        data = {}
        time = 0
        for task in tasks:
            data[task] = 1 + data.get(task,0)
        maxHeap = []
        for cnt in data.values():
            heapq.heappush(maxHeap, -cnt)
        # heapq.heapify(maxHeap)
        q = deque()
        while maxHeap or q:
            time+=1
            if maxHeap:
                val = 1+ heapq.heappop(maxHeap)
                if val:
                    q.append([val,time+n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap,q.popleft()[0])
            
        return time


        