class Twitter:

    def __init__(self):
        self.users_to_tweets = {}
        self.users_to_followers = {}
        self.time = 0 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1 

        if userId not in self.users_to_tweets:
            self.users_to_tweets[userId] = [(-self.time, tweetId)]
            return

        self.users_to_tweets[userId].append((-self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        followers = self.users_to_followers.get(userId, set())
        if userId not in followers:
            followers.add(userId)
        followers = list(followers)
        tweets = []
        for follower_id in followers:
            tweets.extend(self.users_to_tweets.get(follower_id, []))

        heapq.heapify(tweets)

        print(tweets)

        res = []
   
        while tweets and len(res) < 10:
            res.append(heapq.heappop(tweets)[1])

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users_to_followers:
            self.users_to_followers[followerId] = set([followeeId])
            return 

        self.users_to_followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users_to_followers:
            return 
        if followeeId not in self.users_to_followers[followerId]:
            return
        self.users_to_followers[followerId].remove(followeeId)
        
