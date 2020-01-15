class Solution:
	def kthLargest(self, nums, k):
		return sorted(nums)[len(nums)-k]
