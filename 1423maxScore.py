'''
keys: 
Solutions:
Similar: 
T:
S:
'''
from typing import List


class Solution:
	'''
	sliding window
	Find the smallest subarray sum of length len(cardPoints) - k
	https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/discuss/597763/Python3-Easy-Sliding-Window-O(n)%3A-Find-minimum-subarray
    '''
    # T: O(n), S: O(1)
    def maxScore(self, cardPoints: List[int], k: int) -> int:
    	size = len(cardPoints) - k
    	minSubSum = float("inf")
    	l = curSum = 0 # curSum is the sum of current subarray
    	for r, val in enumerate(cardPoints):
    		curSum += val
    		if r - l + 1 > size: # while also works but not necessary cause we increase 1 each time
    			curSum -= cardPoints[l]
    			l += 1
    		if r - l + 1 == size:
    			minSubSum = min(minSubSum, curSum)
    	return sum(cardPoints) - minSubSum


    # memo
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k == len(cardPoints):
            return sum(cardPoints)

        @lru_cache(None)
        def dfs(l, r, k, res = 0):
            if k == 0: # done choosing
                return 0
            # choose left and move l by +1 or choose right and move r by -1
            res = max(cardPoints[i] + dfs(l + 1, r, k - 1), cardPoints[j] + dfs(l, r - 1, k - 1))
            return res   
			
        return dfs(0, len(cardPoints) - 1, k)

        