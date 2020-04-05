'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
    """
    @param s: the given string
    @return: if a permutation of the string could form a palindrome
    """
    def canPermutePalindrome(self, s):
        # write your code here
        import collections
        dict_ = collections.Counter(s)
        return sum(v % 2 for v in dict_.values()) < 2

