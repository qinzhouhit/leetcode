'''
keys:
Solutions:
Similar: 23, merge k sorted linked list
T:
S:
'''
from typing import List


class Solution:
	# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/discuss/84551/simple-Java-O(KlogK)-solution-with-explanation
	# optimal, O(klogk) solution
	def kSmallestPairs2(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
		minHeap = []
        res = []
        if not nums1 or not nums2 or not k:
            return []
        for i in range(min(k, len(nums1))):
            # since the minimum sum will alaways be some number + the 1st element in nums2
            heappush(minHeap, (nums1[i]+nums2[0], nums1[i], nums2[0], 0))
        while k > 0 and minHeap:
            k -= 1
            cur = heappop(minHeap)
            res.append([cur[1], cur[2]])
            if cur[3] == len(nums2) - 1:
                continue # reaching the end of nums2
            # move to the next number in nums2
            nxt_nums2_idx = cur[3] + 1
            heappush(minHeap, (cur[1]+nums2[nxt_nums2_idx], cur[1], nums2[nxt_nums2_idx], nxt_nums2_idx))
        return res




	# educative.io version
	# T: O(N*M*logk), N and M for number of elements in nums1 and nums2
	# S: O(k) for the heap
	def kSmallestPairs1(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
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
			res.append([nums1, nums2])
		return res


	# brute force
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heapify(nums1)
        heapify(nums2)
        ct = 0
        res = []
        minHeap = []
        for num1 in nums1:
            for num2 in nums2:
                heappush(minHeap, (num1+num2, (num1, num2)))
        while minHeap and ct < k:
            _, (num1, num2) = heappop(minHeap)
            res.append([num1, num2])
            ct += 1
        return res

