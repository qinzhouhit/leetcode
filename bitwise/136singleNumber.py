'''
keys:
Solutions:
Similar:
T: O(n)
S: O(1)
'''

from functools import reduce
import operator

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        for i, c in Counter(nums).items():
            if c == 1:
                return i


    # some other solutions; O(N) for S and T
    def singleNumber1(self, nums):
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0)+1
        for key, val in dic.items():
            if val == 1:
                return key

    # T: O(N), S: O(1)
    def singleNumber2(self, nums):
        # the key is associativity law for xor operation
        # so, x ^ x = 0, 0 ^ x = x, odd number of x will be left.
        res = 0
        for num in nums:
            res ^= num # res=0; res^=2 => res=2; res^=2 => res=0
        return res


    def singleNumber3(self, nums):
        return 2*sum(set(nums))-sum(nums)

    def singleNumber4(self, nums):
        return reduce(lambda x, y: x ^ y, nums)

    def singleNumber(self, nums):
        return reduce(operator.xor, nums)
