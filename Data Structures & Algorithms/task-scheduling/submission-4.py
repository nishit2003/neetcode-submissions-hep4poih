class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        
        freq = {}
        for task in tasks:
            freq[task] = 1 + freq.get(task,0)
        
        maxheap = []
        for task,cnt in freq.items():
            maxheap.append(-cnt)
        heapq.heapify(maxheap)

        queue = deque() #[timeidle, temp]

        while maxheap or queue:
            time+=1
            if maxheap:
                temp = 1 + heapq.heappop(maxheap)
                if temp:
                    queue.append([time+n,temp])
            if queue and queue[0][0] == time:
                heapq.heappush(maxheap,queue.popleft()[1])
        return time
