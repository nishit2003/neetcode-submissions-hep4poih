class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        print(f"printing res {res}")
        for i in range(1,len(intervals)):
            prev = res[-1]
            print(prev)
            curr = intervals[i]
            print(curr)
            if prev[1] >= curr[0]:
                res[-1] = [min(prev[0],curr[0]),max(prev[1],curr[1])]
            else:
                res.append(curr)

        return res