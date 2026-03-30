class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        data = defaultdict(int)
        for task in tasks:
            data[task] +=1
        # print(data)
        maxheap = []
        # make heap
        for key,val in data.items():
            heapq.heappush(maxheap, -val)
        # print(minheap)

        queue = deque() #pair of time, task

        while queue or maxheap:
            time += 1
            if maxheap:
                tmp = 1 + heapq.heappop(maxheap)
                if tmp:
                    queue.append([time+n,tmp])
            
            if queue and queue[0][0] == time:
                heapq.heappush(maxheap, queue.popleft()[1])
        return time

