'''
keys: 
Solutions:
Similar: 
T:
S:
'''
from typing import List

# https://leetcode.com/problems/second-largest-digit-in-a-string/discuss/1118774/JavaPython-3-Time-O(n)-space-O(1)-code.
class Solution:
    def secondHighest(self, s: str) -> int:
    	# first: largest, second: second largest
    	first = second = -1
    	for c in s:
    		if c.isdigit():
    			num = ord(c) - ord("0")
    			if num > first:
    				second = first
    				first = num
    			elif second < num < first: 
    				second = num
    			# if num == first or num == second, we dont update
    	return second


