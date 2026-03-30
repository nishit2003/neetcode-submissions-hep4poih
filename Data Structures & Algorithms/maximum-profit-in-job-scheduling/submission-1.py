class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        interval = sorted(zip(startTime, endTime, profit))
        cache = {}
        # print(interval)
        # res = 0

        def dfs(i):
            # nonlocal res
            # res = 0
            if i == len(interval):
                return 0
            if i in cache:
                return cache[i]
            
            # dont include
            res = dfs(i+1)

            # include
            j= i+1
            while j < len(interval):
                if interval[i][1] <= interval[j][0]:
                    break
                j+=1

            cache[i] = res = max(res, interval[i][2] + dfs(j))
            return res

        return dfs(0)