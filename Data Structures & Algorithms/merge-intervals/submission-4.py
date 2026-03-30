class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for i in range(1,len(intervals)):
            curr =intervals[i]
            if curr[0] <= res[-1][1]:
                res[-1] = [min(res[-1][0],curr[0]),max(res[-1][1],curr[1])]

            else:
                res.append(curr)

        return res