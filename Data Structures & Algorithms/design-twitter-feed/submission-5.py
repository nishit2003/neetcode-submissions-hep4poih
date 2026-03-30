class Twitter:

    def __init__(self):
        self.time = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list) #[time, tweetId]
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.followMap[userId].add(userId)
        for each in self.followMap[userId]:
            if each in self.tweetMap:
                index = len(self.tweetMap[each]) - 1
                time, tweetId = self.tweetMap[each][index]
                minHeap.append([time, tweetId, each, index])
        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            time, tweetId, userId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index > 0:
                new_index = index - 1
                time, tweetId = self.tweetMap[userId][new_index]
                heapq.heappush(minHeap,[time, tweetId, userId, new_index])
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
