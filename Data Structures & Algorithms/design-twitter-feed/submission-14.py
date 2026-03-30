class Twitter:
    def __init__(self):
        self.time = 0
        self.followMap = {}
        self.tweetMap = {}
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweetMap:
            self.tweetMap[userId] = []
        self.tweetMap[userId].append([self.time,tweetId]) #time,tweetId
        self.time-=1


    
    def getNewsFeed(self, userId: int) -> List[int]:
        maxheap = []
        res = []
        if userId not in self.followMap:
            self.followMap[userId] = set()
        self.followMap[userId].add(userId)

        for follower in self.followMap[userId]:
            if follower in self.tweetMap:
                index = len(self.tweetMap[follower]) - 1
                time,tweetid = self.tweetMap[follower][index]
                heapq.heappush(maxheap,[time,tweetid,follower,index])
        
        while maxheap and len(res) < 10:
            time,tweetid,follower,index = heapq.heappop(maxheap)
            res.append(tweetid)

            if index > 0:
                newindex = index - 1
                newtime,newtweet = self.tweetMap[follower][newindex]
                heapq.heappush(maxheap,[newtime,newtweet,follower,newindex])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap:
            self.followMap[followerId] = set()
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
    
