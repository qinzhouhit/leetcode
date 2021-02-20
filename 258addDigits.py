'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:

	# O(1) for S and T
	def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9


	# self-made
    def addDigits(self, num: int) -> int:
        if len(str(num)) == 1:
            return num
        res = 0
        for d in str(num):
            res += int(d)
        return self.addDigits(res)
            
    # another 
    def addDigits(self, num: int) -> int:
        digital_root = 0
        while num > 0:
            digital_root += num % 10
            num = num // 10
            
            if num == 0 and digital_root > 9:
                num = digital_root
                digital_root = 0
                
        return digital_root