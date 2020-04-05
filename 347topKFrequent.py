'''
keys:
Solutions:
Similar:
T:
S:
'''

from collections import defaultdict
from collections import Counter

class Solution:
	def topKFrequent(self, nums, k):
		tmp = {}
		for num in nums:
			if num not in tmp:
				tmp[num] = 1
			else:
				tmp[num] += 1
		freq = {}
		for key, v in tmp.items():
			if v not in freq:
				freq[v] = [key]
			else:
				freq[v].append(key) # k: frequency, v: list of nums

		arr = []
		for i in range(len(nums), 0, -1):
			if i in freq:
				for j in freq[i]:
					arr.append(j)

		return [arr[x] for x in range(0,k)]


	# another version
	def topKFrequent1(self, nums, k):
		frq = defaultdict(list)
		for key, cnt in Counter(nums).items():
			frq[cnt].append(key)

		res = []
		for times in reversed(range(len(nums) + 1)):
			res.extend(frq[times])
			if len(res) >= k: return res[:k]

		return res[:k]

obj = Solution()
print (obj.topKFrequent([1,1,4,6,8,2,2,3], 3))
