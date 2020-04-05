'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
    def lengthOfLastWord(self, s):
        if not s.split():
            return 0
        else:
            return len(s.split()[-1])


obj=Solution()
obj.lengthOfLastWord("Hello World")
