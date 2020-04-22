'''
keys: isalpha() # returns “True” if all characters in the string are alphabets
Solutions:
Similar:
T: O(2^n),  where n is the number of alphabet chars,
because every char can be in 2 states (lower and upper).
S:
'''

class Solution:
    # build incrementally, one character by one character
    def letterCasePermutation1(self, S):
        res = ['']
        for ch in S:
            if ch.isalpha():
                res = [i+j for i in res for j in [ch.upper(), ch.lower()]]
            else:
                res = [i+ch for i in res]
        return res

    # swapcase() method converts all uppercase characters to
    # lowercase and vice versa of the given string, and returns it.
    def letterCasePermutation(self, S):
        res = [S]
        for i, c in enumerate(S):
            if c.isalpha():
                res.extend([s[:i] + s[i].swapcase() + s[i+1:] for s in res])
        return res

obj=Solution()
print(obj.letterCasePermutation1("a4b1"))


