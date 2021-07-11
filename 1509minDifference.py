""" 
keys: 
Solutions:
Similar:
T:
S:
"""


class Solution:
	"""
	https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/discuss/730567/JavaC%2B%2BPython-Straight-Forward
	We have 4 plans:
		kill 3 biggest elements
		kill 2 biggest elements + 1 smallest elements
		kill 1 biggest elements + 2 smallest elements
		kill 3 smallest elements
	"""
	# O(NlogN)
    def minDifference(self, nums: List[int]) -> int:
    	nums.sort()
    	# four cases:
    	# nums[n-4] - nums[0]
    	# nums[n-3] - nums[1]
    	# nums[n-2] - nums[2]
    	# nums[n-1] - nums[3]
        return min(b - a for a, b in zip(nums[:4], nums[-4:]))


    # partial sorting
    # T: O(NlogK)
    # S: O(logK)
    # heapq.nlargest: returned results are descending
    # heapq.nsmallest: returned results are ascending
    def minDifference(self, nums: List[int]) -> int:
    	return min(a - b for a, b in zip(heapq.nlargest(4, nums), heapq.nsmallest(4, nums)[::-1]))



