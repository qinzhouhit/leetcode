'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List

class Solution:
    #  We can use the standard two-pointer approach that starts at the
    #  left and right of the string and move inwards. Whenever there is
    #  a mismatch, we can either exclude the character at the left or
    #  the right pointer. We then take the two remaining substrings and
    #  compare against its reversed and see if either one is a palindrome.
    def validPalindrome2(self, s):
        # Time: O(n)
        # Space: O(n)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]: # one: delete right, two: delete left
                one, two = s[left:right], s[left + 1:right + 1]
                return one == one[::-1] or two == two[::-1]
            left, right = left + 1, right - 1
        return True


    # greedy; O(N) for T and O(1) for S
    def validPalindrome1(self, s: str) -> bool:
        
        def isPali(i, j):
            return all(s[k] == s[j-k+1] for k in range(i, j))
        
        for i in range(len(s)//2):
            if s[i] != s[~i]: # ~ means counting from the end of the string
                j = len(s) - 1 - i
                return isPali(i+1, j) or isPali(i,j-1)
        return True



    # TLE; O(N^2) for T and O(N) for S
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            t = s[:i] + s[i+1:]
            if t == t[::-1]: return True

        return s == s[::-1]
