class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        history = sorted(zip(timestamp,username,website))
        sites = {}
        for t,uname,site in history:
            if uname not in sites: 
                sites[uname] = []
            sites[uname].append(site)

        patterns = {}
        for each in sites:
            curr = sites[each]
            n = len(curr)
            for i in range(n):
                for j in range(i+1,n):
                    for k in range(j+1,n):
                        triplet = (curr[i],curr[j],curr[k])
                        print(triplet)
                        if triplet not in patterns:
                            patterns[triplet] = set()
                        patterns[triplet].add(each)
        print(patterns)
        res = []
        maxlen = 0
        for pat in patterns:
            users = patterns[pat]
            if len(users)>maxlen or len(users) == maxlen and pat < res:
                maxlen = len(users)
                res = pat
        return list(res)
