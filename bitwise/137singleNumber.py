'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


from collections import Counter
class Solution:
    # educative.io version
    # where we return the two numbers
    # O(1) for S and O(N) for T
    def singleNumber4(self, nums: List[int]) -> int:
        n1xn2 = 0
        for num in nums:
            n1xn2 ^= num # n1 xor n2 since other number appear in pair
        # get the rightmost bit that is 1
        rightmost_bit = 1
        while rightmost_bit & n1xn2 == 0: 
            rightmost_bit = rightmost_bit << 1 # move bit "1" to left by one
        num1, num2 = 0, 0
        for num in nums:
            if (num & rightmost_bit) != 0:
                num1 ^= num 
            else:
                num2 ^= num
        return num1, num2 # but not sure which one is the first number

    # TODO: bitwise operator
    # O(1) for S and O(N) for T
    def singleNumber3(self, nums: List[int]) -> int:
        seen_once = seen_twice = 0
        for num in nums:
            seen_once = ~seen_twice & (seen_once ^ num)
            seen_twice = ~seen_once & (seen_twice ^ num)
        return seen_once

    # TODO: intuitive bitwise operation
    # working for python
    def singleNumber2(self, nums: List[int]) -> int:
        res = 0
        for i in range(32): # 32 bits for integer
            sum_ = 0
            for num in nums:
                # num >> i & 1: get the i-th bit of the num
                sum_ += (num >> i) & 1 # sum of all i-th bits
            rem = sum_ % 3 # get the remainder of sum_ divided by 3
                # actually the remainder can only be 1 since we only have
                # that x appearing once, the rest numbers all appear three times
                # their remainder will be 0, the only remainder comes from this x
            if i == 31 and rem:
                res -= 1 << 31 # if the input is negative, but why???
            else:
                res = res | rem * (1 << i) # return the i-th bit into res
        return res


    # TODO: hashmap
    # O(N) for S and T
    def singleNumber1(self, nums: List[int]) -> int:
        hashmap = Counter(nums)
        for i in hashmap.keys():
            if hashmap[i] == 1:
                return i

    # TODO: hashset
    # O(N) for S and T
    def singleNumber(self, nums: List[int]) -> int:
        return (3*sum(set(nums)) - sum(nums)) // 2

sol = Solution()
print (sol.singleNumber2([-2,-2,1,1,-3,1,-3,-3,-4,-2]))
