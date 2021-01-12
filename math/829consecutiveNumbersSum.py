'''
keys: 
Solutions:
Similar:
T:
S:
'''
from typing import List



class Solution:
	# sum of first k naturanl numbers
	# T: O(sqrt(N)), S: O(1)
	# N = (x+1) + (x+2) + ... + (x+k)
	# N = k*x + (1+2+...+k)
	# N = kx + k(k+1)/2
	# 2N = k(2x + k + 1)
	# find all possible pairs of k and 2x+k+1 which are both divisors of 2N
	# we only need to iterate up to sqrt(N) in finding divisor of N
	# x = N/k - k(k+1)/2
	# x >= 0 => N/k >= k(k+1)/2
	# 2N + 1/4 >= (k+1/2)^2
	# k <= sqrt(2N + 1/4) - 1/2
    def consecutiveNumbersSum(self, N: int) -> int:
    	ct = 0
    	# x > 0 --> N/k - (k + 1)/2 > 0
    	upper_limit = ceil( (2*N + 1/4)**0.5 - 0.5 ) + 1 # int / ceil, the same
    	for k in range(1, upper_limit):
    		# x should be integer
    		# kx = N - k(k+1)/2
    		if (N - k*(k+1)//2) % k == 0:
    			ct += 1
    	return ct
        