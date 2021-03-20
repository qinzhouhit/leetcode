'''
keys:
Solutions:
Similar:
T:
S:
'''


'''
Integer array, target number 

how many pairs (A[i]+ A[j] == target number) i!=j

                    index: 0,2   1,2
[1,1,2,3,0]  3 ===> value: 1,2   1,2  3,0  == > 3
'''

def pairNum(arr, target):
    # n = len(arr), two loops: O(n^2)
    # time complexity better: O(n)
    # one pass
    # hashmap: {1:2, 2:1, 3:1, 0:1}, ct += 2
    
    
    '''
    for idx, val in enumerate(arr):
        if target - val in hashmap:
            tmp_ct = hashmap[val]
            tmp_ct -= 1
            hashmap[val] = tmp_ct
    '''
    if not arr:
        return -1
    num_ct = {}
    for num in arr:
        if num not in num_ct: # Counter()  # 
            num_ct[num] = 1
        else:
            num_ct[num] += 1
        # if target - num in num_ct:
        #     num_ct[num] -= 1
        #     ct += 1
    ct = 0
    # num_ct: {1:2, 2:1, 3:1, 0:1}, ct += 2
    # [1,1,2,3,0]  3 ===> value: 1,2   1,2  3,0  == > 3
    for num in arr: # 1 
        if target - num in num_ct:
            tmp_ct = num_ct[num]
            tmp_ct -= 1
            num_ct[num] = tmp_ct
            # num_ct[num] -= 1
            if tmp_ct == 0:
                del num_ct[num]
            ct += 1
    return ct
    
            
            
        
        


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


