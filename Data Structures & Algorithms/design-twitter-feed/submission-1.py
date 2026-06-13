class Twitter:
    def __init__(self):
        self.following = {}
        self.feed = deque()

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feed.appendleft((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        userFeed = []
        follows = self.following.get(userId, [])

        for uid, tid in self.feed:
            if uid == userId or uid in follows:
                userFeed.append(tid)
                if len(userFeed) == 10:
                    return userFeed

        return userFeed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = []
        if followeeId not in self.following[followerId]:
            self.following[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            if followeeId in self.following[followerId]:
                self.following[followerId].remove(followeeId)