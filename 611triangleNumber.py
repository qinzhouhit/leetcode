'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
	# brute force, LTE
	# T: O(n^3), S: O(1)
    def triangleNumber(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if nums[i] + nums[j] > nums[k] and \
                        nums[i] + nums[k] > nums[j] and \
                        nums[j] + nums[k] > nums[i]:
                        res += 1
        return res


    # T: O(n^2) for two pointers
    # https://leetcode.com/problems/valid-triangle-number/discuss/104174/Java-O(n2)-Time-O(1)-Space
    '''
    arr = [3, 4, 6, 38, 39 ]
    now your low = 3, high = 38, arr[i] = 39
    Triangle inequality says that any 2 sides of triangle should be greater than the 3rd side.
    you now know that your array is sorted so 3 + 38 > 39 [3, 38, 39] and the numbers which 
    would come after 3 would be greater than 3 so next possible sides of triangles would 
    include [4, 38, 39] , [6, 38, 39]. That is why you add the difference of high - low 
    which is in this case 3 - 0 = 3 possible sides of triangles as shown above.
    '''
    def triangleNumber(self, nums: List[int]) -> int:
    	nums.sort()
    	res, n = 0, len(nums)
    	for i in range(n-1, 1, -1): # i is the 3rd edge, min value as nums[2], so l and r can be nums[0], nums[1]
    		l, r = 0, i-1
    		while l < r:
    			if nums[l] + nums[r] > nums[i]:
    				res += r - l # all the vals in between will also work, just increase l
    				r -= 1 
    			else: # nums[l] + nums[r] <= nums[i], increase left boundary
    				l += 1
    	return res


   	# official O(n^2)
    def triangleNumber(self, nums: List[int]) -> int:
    	nums.sort()
    	res = 0; n = len(nums)
    	for i in range(n-2):
    		k = i + 2
    		for j in range(i+1, n-1):
    			if nums[i] != 0:
    				while k < n and nums[i] + nums[j] > nums[k]:
    					k += 1
    				res += k - j - 1
    	return res




