class Twitter:
    def __init__(self):
        self.time = 0
        self.TweetMap = defaultdict(list) #[time, tweetId]
        self.FollowMap = defaultdict(set)
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.TweetMap[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.FollowMap[userId].add(userId)
        res = []
        maxheap = []
        for followee in self.FollowMap[userId]:
            if followee in self.TweetMap:
                index = len(self.TweetMap[followee]) - 1
                time, tweetId = self.TweetMap[followee][index]
                heapq.heappush(maxheap,[time,tweetId,followee,index])
        print(maxheap)
        while maxheap and len(res) < 10:
            time,tweetId,followee,index = heapq.heappop(maxheap)
            res.append(tweetId)
            if index > 0:
                newIdx = index - 1
                newTime, newTweetId = self.TweetMap[followee][newIdx]
                heapq.heappush(maxheap,[newTime,newTweetId,followee,newIdx])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.FollowMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.FollowMap[followerId]:
            self.FollowMap[followerId].remove(followeeId)
