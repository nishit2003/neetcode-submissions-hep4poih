class Twitter:
    def __init__(self):
        self.time = 0
        self.TweetMap = {} #[time,tweetid]
        self.FollowMap = {}     

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.TweetMap:
            self.TweetMap[userId] = []
        self.TweetMap[userId].append([self.time,tweetId])
        self.time-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.FollowMap:
            self.FollowMap[userId] = set()
        self.FollowMap[userId].add(userId)
        res = []
        maxheap = []
        for followee in self.FollowMap[userId]:
            if followee in self.TweetMap:
                index = len(self.TweetMap[followee]) - 1
                time,tweetid = self.TweetMap[followee][index]
                heapq.heappush(maxheap,[time,tweetid,followee,index])

        while maxheap and len(res) < 10:
            time,tweetid,followee,index = heapq.heappop(maxheap)
            res.append(tweetid)
            if index > 0:
                newIdx = index - 1
                newtime,newtweetid = self.TweetMap[followee][newIdx]
                heapq.heappush(maxheap,[newtime,newtweetid,followee,newIdx])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.FollowMap:
            self.FollowMap[followerId] = set()
        self.FollowMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.FollowMap[followerId]:
            self.FollowMap[followerId].remove(followeeId)
