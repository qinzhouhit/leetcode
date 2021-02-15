'''
keys:
Solutions:
Similar: 373
T:
S:
'''
from typing import List



class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        
        rows, cols = len(mat), len(mat[0])
        if rows == 1:
            return mat[0][k-1] # boring corner case, just one row
        res = mat[0] # first row
        for r in range(1, rows):
        	res = self.kSmallestPairs373(res, mat[r], k) # row_0, row_r
        return res[-k]


    def kSmallestPairs373(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
		minHeap = []
		for i in range(0, min(k, len(nums1))):
			for j in range(0, min(k, len(nums2))):
				if len(minHeap) < k: # only maintain size k
					heappush(minHeap, -(nums1[i]+nums2[j], nums[i], nums[j]))
				else: # already k tuples
					if -(nums1[i] + nums2[j]) < minHeap[0][0]: # < or <=, does not matter
						break # a larger sum appears
					else: # a smaller sum appears, update the heap
						heappop(minHeap)
						heappush(minHeap, (-(nums1[i] + nums2[j]), nums[i], nums[j]))
		res = []
		for _, (nums1, nums2) in minHeap:
			res.append(nums1 + nums2) # here we directly return sum
		return res





