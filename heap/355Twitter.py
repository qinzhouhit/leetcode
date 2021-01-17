'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List
import collections

# https://leetcode.com/problems/design-twitter/discuss/82831/Simple-and-Clean-Python-code-O(logK)-for-getting-news-feed
# the time complexity for building a heap is O(n), insert and remove are O(logn)
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = 0
        self.tweets = collections.defaultdict(list)
        self.following = collections.defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.time -= 1 # posting time, the smaller the latest, using heapq, minHeap
        self.tweets[userId].append((self.time, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        h = []
        # notice that if there is no followers, then it shows the tweets of the user herself.
        people = self.followee.get(user, set()) | set([user])
        for personID in people:
        	if personID in self.tweets and self.tweets[personID]:
        		# Only keep the lastest one to save space, since the latest one will always 
        		# be some tweet from someone. Once poping that tweet, the 2nd latest tweet
        		# of that person will be pushed.
        		# One can also directly push all tweets in the heap
        		time, tweet = self.tweets[personID][-1] 
        		heapq.heappush(h, (time, tweet, personID, len(self.tweets[personID])-1))
        # heapq.heapify(h)
        news = []
        for _ in range(10):
        	if h:
        		time, tweet, person, idx = heapq.heappop(h)
        		news.append(tweet)
        		if idx:
        			new_time, new_tweet = self.tweets[person][idx-1]
        			heapq.heappush(h, (new_time, new_tweet, person, idx-1))
        return news
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.following:
        	self.following[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)