class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = {}
        # for num in nums:
        #     # count[num]+=1
        #     count[num] = 1 + count.get(num,0)

        # heap = []
        # # print(count)
        
        # for num in count.keys():
        #     heapq.heappush(heap, (count[num],num))
        #     if len(heap) > k:
        #         heapq.heappop(heap)

        # res = []
        # for i in range(k):
        #     res.append(heapq.heappop(heap)[1])
        # return res

        count = defaultdict(int)
        res = []
        for num in nums:
            count[num]+=1
        # {1: 1, 2: 2, 3: 3})
        S_count = sorted(count.items(), key = lambda item:item[1], reverse = True)
        print(S_count)

        return [item[0] for item in S_count[:k]]
