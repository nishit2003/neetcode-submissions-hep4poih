class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        arr = sorted(zip(timestamp, username, website))
        mp = defaultdict(list)
        for time, user, site in arr:
            mp[user].append(site)
        # print(mp)
        cnt = defaultdict(list)

        for user in mp:
            pattern = set()
            curr = mp[user]
            for i in range(len(curr)):
                for j in range(i+1,len(curr)):
                    for k in range(j+1,len(curr)):
                        pattern.add((curr[i],curr[j],curr[k]))
        
            for p in pattern:
                cnt[p].append(user)
            print(cnt)
        
        maxcnt = 0
        result = ()
        for pat,users in cnt.items():
            freq = len(users)
            if freq > maxcnt or (freq == maxcnt and pat < result):
                maxcnt = freq
                result = pat
        return list(result)

        

        