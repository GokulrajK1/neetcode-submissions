class Twitter:

    def __init__(self):
        self.time = 0
        self.user_to_tweets = defaultdict(list)
        self.followers = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_to_tweets[userId].append((tweetId, self.time))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followers = self.followers[userId] | set([userId])
        max_heap = []
        for follower in followers:
            tweets = self.user_to_tweets[follower]
            if not tweets:
                continue
            heapq.heappush(max_heap, (-tweets[-1][1], tweets[-1][0], len(tweets) - 2, follower))

        res = []
        while max_heap and len(res) < 10:
            _, tweet_id, index, follower_id = heapq.heappop(max_heap)
            res.append(tweet_id)
            if index < 0:
                continue 
            print(index)
            tweet = self.user_to_tweets[follower_id][index]
            
            heapq.heappush(max_heap, (-tweet[1], tweet[0], index - 1, follower_id))

        return res 
            


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
