'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List

from heapq import *


# T: O(K*logK+(N−K)*logK), asymptotically to O(N*logK)
# S: O(K) for the minHeap
def find_k_largest_numbers(nums, k):
	minHeap = []
	for i in range(k): # # K*logK
		heappush(minHeap, nums[i])
	# O((N−K)*logK)
	for i in range(k, len(nums)):
		if nums[i] > minHeap[0]:
			heappushpop(minHeap, nums[i])
	return list(minHeap)


# Kth smallest number version
def find_k_largest_numbers1(nums, k):
	maxHeap = []
	for i in range(k):
		heappush(maxHeap, -nums[i])
	for i in range(k, len(nums)):
		if -nums[i] > maxHeap[0]:
			heappushpop(maxHeap, -nums[i])
	return list(maxHeap)