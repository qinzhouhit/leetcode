'''
keys: two pointers
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
	# official, T: O(N), S: O(1)
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        res = l = 0
        while l < n:
            r = l
            if r < n - 1 and arr[r] < arr[r+1]:
            	# increasing side of the mountain
                while r < n - 1 and arr[r] < arr[r+1]:
                    r += 1
                # and then, decreasing side of the mountain
                if r < n - 1 and arr[r] > arr[r+1]:
                    while r < n - 1 and arr[r] > arr[r+1]:
                        r += 1
                    # the while loop is broke since we have arr[r] <= arr[r+1]
                    res = max(res, r - l + 1)
            l = max(r, l + 1) # l + 1 since we dont want check the same l again..
        return res



    # two pass
    '''
    In this problem, we take one forward pass to count up hill length (to every point).
	We take another backward pass to count down hill length (from every point).
	Finally a pass to find max(up[i] + down[i] + 1) where up[i] and down[i] should be positives.
	'''
	def longestMountain(self, A):
        up, down = [0] * len(A), [0] * len(A)
        for i in range(1, len(A)):
            if A[i] > A[i - 1]: 
            	up[i] = up[i - 1] + 1
        for i in range(len(A) - 1)[::-1]:
            if A[i] > A[i + 1]: 
            	down[i] = down[i + 1] + 1
        return max([u + d + 1 for u, d in zip(up, down) if u and d] or [0])

    # ONE PASS, and O(1) space
    '''
    In this solution, I count up length and down length.
	Both up and down length are clear to 0 when A[i - 1] == A[i] or 
	down > 0 && A[i - 1] < A[i].
	'''
	def longestMountain(self, A):
        res = up = down = 0
        for i in range(1, len(A)):
            if down and A[i - 1] < A[i] or A[i - 1] == A[i]: up = down = 0
            up += A[i - 1] < A[i]
            down += A[i - 1] > A[i]
            if up and down: res = max(res, up + down + 1)
        return res



    # algoexpert
    def longestMountain(self, arr: List[int]) -> int:
    	res = 0
    	i = 1
    	while i < len(arr) - 1:
    		isPeak = arr[i - 1] < arr[i] and arr[i] > arr[i + 1]
    		if not isPeak:
    			i += 1
    			continue

    		l = i - 2
    		while l >= 0 and arr[l] < arr[l+1]:
    			l -= 1
    		r = i + 2
    		while r < len(arr) and arr[r] < arr[r-1]:
    			r += 1
    		curLen = r - l - 1
    		res = max(res, curLen)
    		i = r
    	return res
















