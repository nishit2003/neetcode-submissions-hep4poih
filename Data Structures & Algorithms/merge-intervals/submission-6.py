class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for i in range(1,len(intervals)):
            prev = res[-1]
            if intervals[i][0] <= prev[1]:
                res[-1] = [min(prev[0],intervals[i][0]),max(prev[1],intervals[i][1])]

            else:
                res.append(intervals[i])
        return res