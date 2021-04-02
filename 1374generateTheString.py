'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
	# O(N) for S and T
    def generateTheString(self, n: int) -> str:
        if n % 2:
            return "a"*n
        else:
            return "b" + self.generateTheString(n-1)


    def generateTheString(self, n: int) -> str:
    	if n % 2 == 1:
            return 'a' * n
        else:
            return 'a' * (n-1) + 'b'