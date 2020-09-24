'''
keys: graph traversal
Solutions:
Similar:
T:
S:
'''
from typing import List
# OA question
'''
nums = [5, 4, 4, 3, 1], num = 2
you can assign num to nums, i.e.,
making [5, 4, 4, 4, 1], leaving 1 to allocate -> 3 fours
or making [5, 5, 5, 3, 1], no remaining to allocate -> 3 fives
maximum number of equal elements in the list is 3.
'''

from collections import Counter
class Solution:

    def allocate(self, nums: List[int], num: int) -> int:
        if not nums:
            return 0
        ct = Counter(nums)
        ct_sort = sorted(ct.items(), key = lambda x: x[1])
        for i in range(len(ct_sort)):
            if ct_sort[i][0] > num:
                continue
            