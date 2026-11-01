class User:
    def __init__(self):
        self.following = set()
        self.posts = []

class Twitter:

    def __init__(self):
       self.posts = deque()
       self.idm = defaultdict(User)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.idm[userId].posts.append(tweetId)
        self.posts.appendleft((userId,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        following = self.idm[userId].following
        res = []
        count = 0
        for uid, tid in self.posts:
            if uid == userId or uid in following:
                count += 1
                res.append(tid)
                if count == 10: break
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.idm[followerId].following.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.idm[followerId].following.discard(followeeId)
        
