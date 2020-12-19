'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List

from heapq import *
class Solution:
	# educative.io version
	# heap version
	# T: O(N*logM), N as total number of elements and M as number of lists
	# N for remove/add one element in the heap
	# S: O(M) for the heap
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
    	minHeap = []
    	start, end = 0, float("inf")
    	curMax = -float("inf")
    	# put the 1st element of each array in the heap
    	for arr in nums:
    		heappush(minHeap, (arr[0], 0, arr)) # one can also just store row idx here
    		curMax = max(curMax, arr[0])
        # pop the smallest, update the range if shrinks
        while len(minHeap) == len(nums): # it ends when one list reaches the end
        	num, i, arr = heappop(minHeap)
        	if curMax - num < end - start:
        		start = num
        		end = curMax
        	if len(arr) > i+1:
        		heappush(minHeap, (arr[i+1], i+1, arr))
        		curMax = max(curMax, arr[i+1])
        return [start, end]

    # the version only sotring the row idx, better space complexity
    def smallestRange1(self, nums: List[List[int]]) -> List[int]:
    	minHeap = []
        right = -float("inf")
        for idx, row in enumerate(nums):
            heappush(minHeap, (row[0], idx, 0)) # 0 as the column idx
            right = max(right, row[0])
        ans = 0, float("inf")
        while len(minHeap) == len(nums):
            left, row_idx, col_idx = heappop(minHeap)
            if right - left < ans[1] - ans[0]:
                ans = left, right
            if col_idx + 1 < len(nums[row_idx]):
                heappush(minHeap, (nums[row_idx][col_idx+1], row_idx, col_idx+1))
                right = max(right, nums[row_idx][col_idx+1])
        return ans

    # https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/discuss/104904/Python-Heap-based-solution
    # a concise version, faster
	def smallestRange2(self, nums: List[List[int]]) -> List[int]:
    	minHeap = []
        right = -float("inf")
        for idx, row in enumerate(nums):
            heappush(minHeap, (row[0], idx, 0)) # 0 as the column idx
            right = max(right, row[0])
        ans = 0, float("inf")
        while minHeap:
            left, row_idx, col_idx = heappop(minHeap)
            if right - left < ans[1] - ans[0]:
                ans = left, right
            if col_idx + 1 == len(nums[row_idx]):
            	return ans
            # i.e., when col_idx + 1 < len(nums[row_idx])
            heappush(minHeap, (nums[row_idx][col_idx+1], row_idx, col_idx+1))
            right = max(right, nums[row_idx][col_idx+1])
        return ans





