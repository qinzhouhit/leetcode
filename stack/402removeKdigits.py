'''
keys: greedy + stack
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
	# official, O(n) for S and T, N as the length of digits
    def removeKdigits(self, num: str, k: int) -> str:
        numStack = []
        
        # Construct a monotone increasing sequence of digits
        for digit in num:
            while k and numStack and digit < numStack[-1]: # have smmaller digit comming
                numStack.pop() # pop the bigger previous one
                k -= 1
        
            numStack.append(digit)
        
        # - Trunk the remaining/last K digits at the end
        # - in the case k==0: return the entire list
        # The lstrip() method removes any leading characters (space 
        # is the default leading character to remove)
        # this is for cases like num = "9", k = 1, since res should be "0"
        # excluding the last k digits
        finalStack = numStack[:-k] if k else numStack
        
        # trip the leading zeros
        # or "0" is for cases like num = "10", k = 2, res will be ""
        return "".join(finalStack).lstrip('0') or "0"

