class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        arr = sorted(zip(timestamp,username,website))
        sites = defaultdict(list)
        for time, user, site in arr:
            sites[user].append(site)

        pattern = defaultdict(set)
        for each in sites:
            curr = sites[each] 
            res = set()
            n = len(curr)
            for i in range(n):
                for j in range(i+1,n):
                    for k in range(j+1,n):
                        res.add((curr[i],curr[j],curr[k]))
        
            for p in res:
                pattern[p].add(each)
            print(pattern)

        maxcnt = 0
        result = ()
        for pat,users in pattern.items():
            freq = len(users)
            if freq > maxcnt or (freq == maxcnt and pat < result):
                maxcnt = freq
                result = pat
        return list(result)


