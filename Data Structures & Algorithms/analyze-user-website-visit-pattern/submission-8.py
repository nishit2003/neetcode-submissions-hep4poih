class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        intervals = sorted(zip(timestamp,username,website))
        sites = {}
        for time,uname,site in intervals:
            if uname not in sites:
                sites[uname] = []
            sites[uname].append(site)
        # print(sites)

        pattern = {}
        
        for each in sites:
            # res = set()
            curr = sites[each]
            n= len(curr)
            for i in range(n):
                for j in range(i+1,n):
                    for k in range(j+1,n):
                        triplet = ((curr[i],curr[j],curr[k]))
                        if triplet not in pattern:
                            pattern[triplet] = set()
                        pattern[triplet].add(each)
        # print(pattern)
        maxlen = 0
        res = []
        for pat in pattern:
            users = pattern[pat]
            if len(users) > maxlen or (len(users) == maxlen and pat < res):
                maxlen = len(users)
                res = pat
        return list(res)
