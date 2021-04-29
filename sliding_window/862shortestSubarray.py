'''
keys: subarray sum => sliding window
Solutions:
Similar: 209
T:
S:
'''
from typing import List
import collections

class Solution:
	# O(N) for S and T
	# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/143726/C%2B%2BJavaPython-O(N)-Using-Deque
	def shortestSubarray(self, A: List[int], K: int) -> int:
		d = collections.deque([[0, 0]]) # [idx, prefixSum]
		res, culSum = float("inf"), 0
		for r, val in enumerate(A):
			culSum += val # prefix sum
			# subarray sum: culSum - d[0][-1]
			# while loops check all the subarray satisfying this condition
			# then shorten the subarray from left
			while d and culSum - d[0][-1] >= K:
				res = min(res, r - d.popleft()[0] + 1)
			# if prefixSum decreases, we pop() to make subarray shorter and sum larger
			# make subarray shorter since future id can subtract a larger id (we pop, make idx larger)
			# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/143726/C++JavaPython-O(N)-Using-Deque/195904
			while d and culSum <= d[-1][1]: # keep prefix sum increasing in deque
				d.pop()
			d.append([r+1, culSum])
		return res if res < float("inf") else -1


	##### geeksforgeeks
	# Returns length of smallest subarray
	# with sum greater than x. If there
	# is no subarray with given sum,
	# then returns n+1
	def smallestSubWithSum(arr, n, x):
	 
	    # Initialize length of smallest
	    # subarray as n+1
	    min_len = n + 1
	 
	    # Pick every element as starting point
	    for start in range(0,n):
	     
	        # Initialize sum starting
	        # with current start
	        curr_sum = arr[start]
	 
	        # If first element itself is greater
	        if (curr_sum > x):
	            return 1
	 
	        # Try different ending points
	        # for curremt start
	        for end in range(start+1,n):
	         
	            # add last element to current sum
	            curr_sum += arr[end]
	 
	            # If sum becomes more than x
	            # and length of this subarray
	            # is smaller than current smallest
	            # length, update the smallest
	            # length (or result)
	            if curr_sum > x and (end - start + 1) < min_len:
	                min_len = (end - start + 1)
	         
	    return min_len;

sol = Solution()
print (sol.shortestSubarray([2,-1,2], 3))
