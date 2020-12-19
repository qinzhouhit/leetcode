'''
keys: 
Solutions:
Similar: 
T:
S:
'''
from typing import List

from heapq import *
# T: O(NlogN) for puting all the elements in the minHeap
# S: O(N)
def find_sum_of_elements(nums, k1, k2):
	heapify(nums)
	for _ in range(k1): # remove the first k1 numbers
		heappop(nums)
	res = 0
	for _ in range(k2 - k1 - 1): # take the next k2-k1-1 numbers
		res += heappop(nums)
	return res

# shrinking the heap space
# T: O(Nlogk2), only put the k2 top numbers in the heap
# S: O(k2)
def find_sum_of_elements1(nums, k1, k2):
	minHeap = []
	for i in range(len(nums)):
		if i < k2 - 1: # 0 to k2 - 2, k2 - 1 numbers in total
			heappush(maxHeap, -nums[i])
		elif nums[i] < -minHeap[0]: # smaller number coming
			heappush(minHeap, -nums[i])
	res = 0
	for _ in range(k2 - k1 - 1):
		res += -heappop(nums)
	return res


