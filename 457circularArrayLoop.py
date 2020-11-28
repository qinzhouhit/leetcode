'''
keys: fast and slow pointers
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
	# T: O(N^2), N = len(nums)
    def circularArrayLoop(self, nums: List[int]) -> bool:

    	def find_nxt(nums, isForward, idx):
    		direction = nums[idx] >= 0
    		if direction != isForward:
    			return -1
    		nxt_idx = (idx + nums[idx]) % len(nums)
    		if nxt_idx == idx:
    			return -1 # the loop contains only one element
    		return nxt_idx

        for i in range(len(nums)):
        	isForward = nums[i] >= 0
        	slow, fast = i, i
        	while True:
        		slow = find_nxt(nums, isForward, slow)
        		fast = find_nxt(nums, isForward, fast)
        		if fast != -1:
        			fast = find_nxt(nums, isForward, fast)
        		if slow == -1 or fast == -1 or slow == fast:
        			break
        	# i.e., show != -1 and fast != -1 and slow == fast
        	if slow != -1 and slow == fast:
        		return True
        return False

