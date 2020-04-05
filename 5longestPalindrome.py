'''
keys: two cases
Solutions:
Similar:
T:
S:
'''


class Solution():
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        print (res)
        return res

    # get the longest palindrome, l, r are the middle indexes
    # from inner to outer
    def helper(self, s, l, r):
        if l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]

obj=Solution()
obj.longestPalindrome('abacddc')

