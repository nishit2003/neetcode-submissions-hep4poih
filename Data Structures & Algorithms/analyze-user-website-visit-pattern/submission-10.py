class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # Submitted by Daksh to check complexity
        
        usersMap=defaultdict(list)
        for user, time, web in zip(username, timestamp, website):
            usersMap[user].append((time, web))
        
        patterns=defaultdict(int)

        def dfs(history,i,path):
            if len(path)==3:
                patterns[tuple(path)]-=1
                return
            if i>=len(history):
                return
            path.append(history[i][1])
            dfs(history, i+1, path)
            path.pop()
            dfs(history, i+1, path)
        
        for user in usersMap.keys():
            # print(user, usersMap[user])
            history = usersMap[user]
            history.sort()
            dfs(history, 0, [])
            # print(patterns)
        
        patternsList = [(score, pattern) for pattern, score in patterns.items()]
        patternsList.sort()
        return list(patternsList[0][1])