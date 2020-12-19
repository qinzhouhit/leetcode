'''
keys: 
Solutions:
Similar:
T:
S:
'''
from typing import List

'''
Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.

Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4], K=5
Output: 4
Explanation: The 5th smallest number among all the arrays is 4, this can be verified from the merged 
list of all the arrays: [1, 2, 3, 3, 4, 6, 6, 7, 8]

Similar questions: find the median of all sorted arrays, i.e., k = N//2
Or merge k sorted arrays.
'''

from heapq import *
# T: O(klogM), S: O(M), dealing with k elements out of all M elements
def find_Kth_smallest(lists, k):
	minHeap = []
	for l in lists:
		for val in l:
			heappush(minHeap, val)
	ct = 0
	while minHeap:
		ct += 1
		val = heappop(minHeap)
		if ct == k:
			return val
	return None


# official, push the tuple is smart, so we dont need to push all the elements
# we only need to push at most k tuples
def find_Kth_smallest1(lists, k):
	minHeap = []
	for i in range(len(lists)):
		heappush(minHeap, (list[i][0], 0, lists[i]))
	numCt, num = 0, 0
	while minHeap:
		num, i, list_ = heappop(minHeap)
		numCt += 1
		if numCt == k:
			break
		if len(list_) > i+1:
			heappush(minHeap, (list[i+1], i+1, list_))
	return number
