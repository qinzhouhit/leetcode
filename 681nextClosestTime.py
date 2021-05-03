'''
keys: 
Solutions:
Similar: 
T:
S:
'''
from typing import List

'''
itertools.product(allowed, repeat = 4)
Cartesian product, equivalent to a nested for-loop
For example, product(arr, repeat=3) means the same 
as product(arr, arr, arr).
'''

class Solution:

    # O(1) for S and T, simulation
    def nextClosestTime(self, time: str) -> str:
        res = start = 60 * int(time[:2]) + int(time[3:])
        elapsed = 24 * 60
        digits = {int(x) for x in time if x != ':'}
        for h1, h2, m1, m2 in itertools.product(digits, repeat = 4):
            hours, mins = 10*h1 + h2, 10*m1 + m2 # h1, h2 are digits
            if hours < 24 and mins < 60:
                cur = hours * 60 + mins
                cur_elapased = (cur - start) % (24 * 60)
                if 0 < cur_elapased < elapsed:
                    res = cur
                    elapsed = cur_elapased
        return "{:02d}:{:02d}".format(*divmod(res, 60))



	# O(1) for S and T, simulation
    def nextClosestTime(self, time: str) -> str:
    	cur = 60 * int(time[:2]) + int(time[3:]) # total minutes
    	digits = {int(x) for x in time if x != ':'}
    	while True:
    		cur = (cur + 1) % (24 * 60)
    		# divmod(cur, 60) -> hours, minutes
    		# divmod(hours, 10) -> digits of hours
    		# divmod(minutes, 10) -> digits of minutes
    		if all(digit in digits \
    				for block in divmod(cur, 60)\
    				for digit in divmod(block, 10)):
    			return "{:02d}:{:02d}".format(*divmod(cur, 60))