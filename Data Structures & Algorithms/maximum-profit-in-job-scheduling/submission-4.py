class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime,endTime,profit))
        cache = {}
        def dfs(i):
            if i == len(intervals):
                return 0
            if i in cache:
                return cache[i]
            # not to include the current job
            res = dfs(i+1)

            # include
            j = i+1
            while j < len(intervals):
                if intervals[j][0] >= intervals[i][1]:
                    break
                j+=1
            
            cache[i] = res = max(res,intervals[i][2] + dfs(j))
            return res
        
        return dfs(0)
