'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List



class Solution:
	# https://leetcode.com/problems/boats-to-save-people/discuss/156740/C%2B%2BJavaPython-Two-Pointers
	# T: O(nlogn)
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1 # l the lightest and r the heaviest  

        # If the heaviest person can share a boat with the lightest person,
        #  then do so. Otherwise, the heaviest person can't pair with anyone, 
        # so they get their own boat.
        ans = 0
        while l <= r:
            ans += 1
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
        return ans


    # intuitive
    def numRescueBoats(self, people: List[int], limit: int) -> int:
    	people.sort()
        l, r = 0, len(people) - 1

        res = 0
        while l <= r:
        	if people[l] + people[r] <= limit:
        		l += 1
        		r -= 1
        	else: # only take the heaviest person
        		r -= 1
        	res += 1 # use one boat
		return res