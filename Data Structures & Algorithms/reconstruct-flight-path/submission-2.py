class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        hashset = defaultdict(list)
        for src, des in tickets:
            hashset[src].append(des)
        for src in hashset:
            hashset[src].sort(reverse=True)
        res = []
        def dfs(src):
            while hashset[src]:
                dfs(hashset[src].pop())
            res.append(src)
        dfs("JFK")
        return res[::-1]
