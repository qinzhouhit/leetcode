'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
	# kmp, O(m), i.e., O(m+m)
	'''
	https://leetcode.com/problems/shortest-palindrome/discuss/60113/Clean-KMP-solution-with-super-detailed-explanation
	# "find the longest palindrome substring starts from index 0".
	We add "#" here to force the match in reverse(s) starts from its first index
	What we do in KMP here is trying to find a match between prefix in s and a 
	postfix in reverse(s). The match part will be palindrome substring.
	'''
	def shortestPalindrome(self, s: str) -> str:

		def getTable(str_): # construct the table of KMP
			n = len(str_)
			table = [0] * n
			idx = 0
			for i in range(n):
				if str_[idx] == str_[i]:
					table[i] = table[i-1] + 1
					idx += 1
				else:
					idx = table[i-1]
					while idx > 0 and str_[idx] != str_[i]:
						idx = table[idx-1]

					if str_[idx] == str_[i]:
						idx += 1
					table[i] = idx
			return table

		tmp = s + "#" + s[::-1]
		table = getTable(tmp)
		return tmp[table[len(table)-1]:][::-1] + s



	# two pointers + recursion
	# T: O(n^2)
	# S: O(n)
	'''
	left idx:  4
	dabe abca ebad
	left idx:  2
	ac ab ca
	left idx:  1
	b a b
	left idx:  1
	'''
	def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        l = 0
        for r in range(n-1, -1, -1):
        	if s[l] == s[r]:
        		l += 1
        if l == n:
        	return s
        remain_rev = s[l: n]
        remain_rev = remain_rev[::-1]
        return remain_rev + self.shortestPalindrome(s[0:l]) + s[l:]



	'''
	brute force
	T: O(n^2) for iteration and comparison
	S: O(n) for rev
	s = "abcd"
	idx rev[i:], s[0:n-i]
	0 dcba abcd 
	1 cba abc 
	2 ba ab 
	3 a a
	idx rev[0:i], s[0:n-i]
	0  abcd
	1 d abc
	2 dc ab
	3 dcb a
	'''
    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]
        n = len(s)
        for i in range(n): # try to find largest palin from the front, so s[0:n] => s[0:1]
            # print (i, rev[0:i], s[0:n-i])
            if s[0:n-i] == rev[i:]: # check the substring is pilandrome or not
                return rev[0:i] + s
        return ""



