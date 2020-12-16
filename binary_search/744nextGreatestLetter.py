'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
	# binary search; T: O(logN), S: O(1)
	def nextGreatestLetter2(self, letters: List[str], target: str) -> str:
		n = len(letters)
		if target > letters[-1] or target < letters[0]: 
            return letters[0]
        l, r = 0, n - 1
        while l <= r:
            m = l + (r - l) // 2
            if letters[m] > target:
                r = m - 1
            else:
                l = m + 1
        return letters[l % n]


    def nextGreatestLetter3(self, letters: List[str], target: str) -> str:
    	index = bisect.bisect(letters, target)
        return letters[index % len(letters)]


	# linear scan; T: O(N), S: O(1)
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    	for c in letters:
    		if c > target:
    			return c
    	return letters[0]

   	# record letter seen; T: O(N), S: O(1)
    def nextGreatestLetter1(self, letters: List[str], target: str) -> str:
    	seen = set(letters)
    	for i in range(1, 26):
    		candidate = chr((ord(target) - ord("a") + i) % 26 + ord("a"))
    		if candidate in seen:
    			return cand




        

        