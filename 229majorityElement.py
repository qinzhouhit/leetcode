'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
	# T: O(N), S: O(1)
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        # 1st pass
        count1, count2, candidate1, candidate2 = 0, 0, None, None
        for cur in nums:
            if candidate1 == cur:
                count1 += 1
            elif candidate2 == cur:
                count2 += 1
            elif count1 == 0: 
                candidate1 = cur
                count1 += 1
            elif count2 == 0:
                candidate2 = cur
                count2 += 1
            else: # new candidate coming, challenging the existing candidates
                count1 -= 1
                count2 -= 1
        
        # 2nd pass
        res = []
        for c in [candidate1, candidate2]:
            if nums.count(c) > len(nums)//3:
                res.append(c)
        return res