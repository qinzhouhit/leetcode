'''
keys: sliding window
Solutions:
Similar:
T: O(n)
S: 
'''

class Solution:
    # return an integer
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}

        for i, c in enumerate(s):
            if c in usedChar and start <= usedChar[c]:
                start = usedChar[c] + 1
            else:
                maxLength = max(maxLength, i - start + 1)
            usedChar[c] = i
        return maxLength


obj=Solution()
obj.lengthOfLongestSubstring('tmmzuxta')
