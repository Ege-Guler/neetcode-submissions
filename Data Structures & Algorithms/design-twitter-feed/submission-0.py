import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.tweets = [] #heap (time, (tweetId,userId))
        self.following = defaultdict(set) #userID -> List[userId]
        self.time = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        
        heapq.heappush(self.tweets, (-self.time, tweetId, userId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        userId_followees = self.following[userId]

        userId_followees.add(userId)
        tmp = self.tweets[:]
        counter = 0
        
        res = []

        while tmp and counter < 10:
            _, tweetId, userId = heapq.heappop(tmp)

            if userId not in userId_followees:
                continue
            
            counter += 1
            res.append(tweetId)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].discard(followeeId)
