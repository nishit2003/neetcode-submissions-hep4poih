class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        for i in range(len(intervals)):
            curr = intervals[i]
            if newInterval[1] < curr[0]: # new - res
                res.append(newInterval)
                return res + intervals[i:] 
            

            elif newInterval[0] > curr[1]: # res - new
                res.append(curr)
            
            else:
                newInterval = [min(newInterval[0],intervals[i][0]),
                max(newInterval[1],intervals[i][1])]
        res.append(newInterval)
        return res