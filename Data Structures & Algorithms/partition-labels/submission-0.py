class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lidx = {}
        for i,v in enumerate(s):
            lidx[v] = i

        res = []
        size = end = 0
        for i,c in enumerate(s):
            size += 1
            end = max(end,lidx[c])

            if i == end:
                res.append(size)
                size = 0

        return res
