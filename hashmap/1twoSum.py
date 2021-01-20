'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution(object):
    # latest one
    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []
        
        hashmap = {}
        for idx, val in enumerate(nums):
            if target-val in hashmap:
                return [hashmap[target-val], idx]
            hashmap[val] = idx
        return []


	# O(N) for S and T
	def twoSum1(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []
        d = {}
        for idx, val in enumerate(nums):
        	# the order of two IF matters, e.g., [3,2,4], 6. swap the order
        	# one would have res as [0, 0]
            if target - val in d:
                return [d[target-val], idx]
            if val not in d:
                d[val] = idx

    # most concise one 
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
    	h = {}
    	for idx, val in enumerate(nums):
    		residue = target - val
    		if residue not in h:
    			h[val] = idx
    		else:
    			return [h[residue], idx]

    # wasted
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i

obj=Solution()
nums=[2,7,11,15]
target=10
obj.twoSum(nums, target)


