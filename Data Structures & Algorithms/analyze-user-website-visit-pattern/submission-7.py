class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        data = sorted(zip(timestamp,username,website))
        sites = {}
        maxcount = 0
        for time,uname,site in data:
            if uname not in sites:
                sites[uname] = []
            sites[uname].append(site)
        # print(sites)

        pattern = defaultdict(set)
        for each in sites:
            curr = sites[each]
            n = len(curr)
            res = set()
            for i in range(n):
                for j in range(i+1,n):
                    for k in range(j+1,n):
                        res.add((curr[i],curr[j],curr[k]))
            
            for everypattern in res:
                pattern[everypattern].add(each)

        for pat,users in pattern.items():
            freq = len(users)
            if freq > maxcount or (freq == maxcount and pat < result):
                maxcount = freq
                result = pat

        return list(result)