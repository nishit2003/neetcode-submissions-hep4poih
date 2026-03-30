class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        res2 = []
        for i in nums:
            res[i] +=1
        
        sorted_items = sorted(res.items(), key = lambda x:x[1], reverse = True)

        for i in range(k):
            res2.append(sorted_items[i][0])

        return res2