'''
keys: dp
Solutions:
Similar: 198
T: 
S: 
'''
from typing import List


class Solution:
	# https://leetcode.com/problems/delete-and-earn/discuss/109895/JavaC%2B%2B-Clean-Code-with-Explanation
	# create buckets and make it similar to 198
	'''
	If we sort all the numbers into buckets indexed by these numbers, 
	this is essentially asking you to repetitively take an bucket while
	 giving up the 2 buckets next to it. 
	'''
	# T: O(N)
	# S: O(10001)
	def deleteAndEarn(self, nums: List[int]) -> int:
		n = 10001
		values = [0] * n
		for num in nums:
			values[num] += num # total sum, not count

		take = 0; skip = 0 
		for _, val in enumerate(values): 
			take_i = skip + val
			skip_i = max(skip, take)
			take = take_i
			skip = skip_i
		return max(take, skip)


    def deleteAndEarn(self, nums: List[int]) -> int:

        count = collections.Counter(nums)
        prev = None
        avoid = using = 0
        for k in sorted(count):
            if k - 1 != prev:
                avoid, using = max(avoid, using), k * count[k] + max(avoid, using)
            else:
                avoid, using = max(avoid, using), k * count[k] + avoid
            prev = k
        return max(avoid, using)