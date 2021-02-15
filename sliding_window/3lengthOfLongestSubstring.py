'''
keys: sliding window
Solutions:
Similar:
T: O(n)
S: 
'''

class Solution:
    # return an integer
    # sliding window
    def lengthOfLongestSubstring(self, s):
        startIdx = maxLength = 0
        usedChar = {}

        for endIdx, c in enumerate(s):
            if c in usedChar and startIdx <= usedChar[c]:
                startIdx = usedChar[c] + 1
            else:
                maxLength = max(maxLength, endIdx - startIdx + 1)
            usedChar[c] = endIdx
        return maxLength


obj=Solution()
obj.lengthOfLongestSubstring('tmmzuxta')
