'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
	# O(N) for S and T
	def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0]*n
        dp[0] = nums[0]
        q = deque([0]) # storing indexes of nums, monotonically decreasing.
        for i in range(1, n):
            # pop the old index
            while q and q[0] < i-k:
                q.popleft() # 
            dp[i] = nums[i] + dp[q[0]]
            # pop the smaller value
            while q and dp[i] >= dp[q[-1]]:
                q.pop()
            q.append(i)
        return dp[-1]


    # huahua
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0]*n # where score[i] represents the max score starting at nums[0] and ending at nums[i].
        dp[0] = nums[0]
        # q will store at most k values
        q = deque([0]) # storing unique values of dp[i-k+1 ~ i] in descending order
        for i in range(1, n):
            dp[i] = nums[i] + dp[q[0]]
            while q and dp[i] >= dp[q[-1]]:
            	q.pop() # pop 
            while q and i - q[0] >= k:
            	q.popleft() # old vals, out of jump range
            q.append(i)
        return dp[-1]


    # LC 239, combining sliding window
    # T: O((n-k)*k), S: O(1), brute force
    # T: O((n-k)*logk), S: O(k), BST/multimap
    # T: O(n), S: O(k), monotonic queue
    def maxResult(self, nums: List[int], k: int) -> int:
    	



    # huahua video TLE version
    # T: O((n-k)*k), S: O(n)
    def maxResult(self, nums: List[int], k: int) -> int:
    	@lru_cache(None)
    	def dp(i):
    		if i == 0:
    			return nums[0]
    		return nums[i] + max(dp(j) for j in range(max(0, i-k), i))
    	return dp(len(nums)-1)
