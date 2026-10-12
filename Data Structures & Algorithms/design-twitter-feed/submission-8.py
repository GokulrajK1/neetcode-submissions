class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followers = self.followers[userId]
        min_heap = []
        if self.tweets[userId]:
            min_heap.append((self.tweets[userId][-1][0], userId, len(self.tweets[userId]) - 2, self.tweets[userId][-1][1]))
        for follower in followers:
            if self.tweets[follower]:
                heapq.heappush(min_heap, (self.tweets[follower][-1][0], follower, len(self.tweets[follower]) - 2, self.tweets[follower][-1][1]))

        res = []
        while min_heap and len(res) < 10:
            time, follower_id, index, tweetId = heapq.heappop(min_heap)
            res.append(tweetId)
            if index < 0:
                continue
            heapq.heappush(min_heap, (self.tweets[follower_id][index][0], follower_id, index - 1, self.tweets[follower_id][index][1]))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
