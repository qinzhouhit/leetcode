'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


# https://leetcode.com/problems/integer-replacement/discuss/87920/A-couple-of-Java-solutions-with-explanations
'''
The infamous test with n=3 fails for that strategy because 
11 -> 10 -> 1 is better than 11 -> 100 -> 10 -> 1. 
1. If n is even, halve it.
2. If n=3 or n-1 has less 1's than n+1, decrement n.
3. Otherwise, increment n.
'''
class Solution:
    def integerReplacement(self, n: int) -> int:
        res = 0
        while n != 1:
        	if n & 1 == 0: # even
        		n >> 1
        	elif n == 3 or bin(n+1).count(1) > bin(n-1).count(1):
        		n -= 1
        	else:
        		n += 1
        	res += 1
        return res







# self-made, not working?
class Solution:
    res = 0
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return self.res
        if n % 2: # odd
            n = n - 1
            self.res += 1
            self.integerReplacement(n)
        else:
            n = n // 2
            self.res += 1
            self.integerReplacement(n)