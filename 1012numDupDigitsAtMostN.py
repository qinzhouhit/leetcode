'''
keys: 
Solutions:
Similar:
T:
S:
'''
from typing import List


"""
The corner case is too hard to manage...

count res as N - total number without duplicated digits.
turns into a math and permutation problem.

select m out of n
P(m, n): n! / (n-m)!

Algorithm:

lets say N has k digits.
1) count number less than k digits
lets say number with i digits
first digit 1 ~ 9, following option is 0 ~ 9 without first digit
count = 9 * P(i-1,9)

2) count number has k digits. 
Calculate digits with same prefix. 
Prefix cannot has duplicate digits.
for case like 77xxx, we should stop the calculation.
"""

class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        def f(n):
            if n == 0 or n == 1: 
            	return 1
            return f(n-1) * n

        # pick m out of n, ordred matters
        def P(m, n): 
        	return f(n) // f(n - m)
        
        # N + 1 as padding.
        nums = [int(d) for d in str(N + 1)]
        K = len(nums) # N has K digits
        cnt = 0 # number with no repeated val
        
        # count **postive number with digits less than K
        for i in range(1, K): 
        	cnt += 9 * P(i-1, 9)
            
        # count number with K digits
        seen = set() # seen digit in prefix
        for i in range(K): 
            # prefix = nums[:i] + currentDigit
            # currentDigit < nums[i]
            for x in range(1 if i == 0 else 0, nums[i]):
                if x in seen: 
                	continue # avoid duplication
                cnt += P(K - (i + 1), 10 - (i + 1))
            
            # since next iteration, prefix has duplicate digits, break
            if nums[i] in seen: 
            	break
            seen.add(nums[i])
        
        return N - cnt




