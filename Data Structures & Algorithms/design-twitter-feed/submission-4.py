class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1 

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = []
        self.followers[userId].add(userId)
        followees = self.followers[userId]
        for followeeId in followees:
            if followeeId not in self.tweets:
                continue
            tweets = self.tweets[followeeId]
            index = len(tweets) - 1
            time, tweetId = tweets[index]
            heapq.heappush(min_heap, (time, tweetId, followeeId, index - 1))

        k = 0
        res = []
        while min_heap and k < 10:
            time, tweetId, followeeId, index = heapq.heappop(min_heap)
            res.append(tweetId)
            new_time, new_tweetId = self.tweets[followeeId][index]
            if index >= 0:
                heapq.heappush(min_heap, (new_time, new_tweetId, followeeId, index - 1))
            k += 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
