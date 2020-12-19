'''
keys: 
Solutions:
Similar: 
T:
S:
'''
from typing import List


'''
Given an array of numbers and a number ‘K’, we need to remove ‘K’ numbers from
 the array such that we are left with maximum distinct numbers.
 Input: [7, 3, 5, 8, 5, 3, 3], and K=2
Output: 3
Explanation: We can remove two occurrences of 3 to be left with 3 distinct 
numbers [7, 3, 8], we have to skip 5 because it is not distinct and occurred twice. 
Another solution could be to remove one instance of '5' and '3' each to be left 
with three distinct numbers [7, 5, 8], in this case, we have to skip 3 because 
it occurred twice.
'''

from collections import Counter
# T: O(NlogN + KlogN), NlogN for pushing in hashmap and minheap, N == len(nums)
# O(KlogN) for taking K nums out from heap
# S: O(N) to store all the characters
def find_maximum_distinct_elements(nums, k):
	distinct_ele_ct = 0
	if len(nums) <= k:
		return distinct_ele_ct
	numFreq = Counter(nums)
	minHeap = []
	for num, freq in numFreq.items():
		if freq == 1:
			distinct_ele_ct += 1
		else:
			heappush(minHeap, (freq, num))
	# try removing the least frequent numbers
	while k > 0 and minHeap:
		freq, num = heappop(minHeap)
		k -= freq - 1 # make freq == 1
		if k >= 0:
			distinct_ele_ct += 1
	# after done with all nums
	if k > 0:
		distinct_ele_ct -= k
	return distinct_ele_ct




