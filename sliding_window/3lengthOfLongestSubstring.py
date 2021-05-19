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
    # T: O(n), S: O(min(m, n)), m as size of charset
    # "tmmzuxt"
    def lengthOfLongestSubstring(self, s):
        startIdx = maxLength = 0
        usedChar = {} # v: latest appearance idx of a character

        for endIdx, c in enumerate(s):
            if c in usedChar and startIdx <= usedChar[c]:
                startIdx = usedChar[c] + 1
            else: # c is new or startIdx > usedChar[c]
                maxLength = max(maxLength, endIdx - startIdx + 1)
            usedChar[c] = endIdx
        return maxLength


    # self-made
    def lengthOfLongestSubstring1(self, s: str) -> int:
        if not s:
            return 0
        
        last_idx = {}
        l = 0
        maxL = 0
        for r, c in enumerate(s):
            if c in last_idx and l <= last_idx[c]:
                l = last_idx[c] + 1
            else:
                maxL = max(maxL, r-l+1)
            last_idx[c] = r
        return maxL


    # official
    def lengthOfLongestSubstring2(self, s: str) -> int:
        chars = [0] * 128 # for frequency track

        left = right = 0

        res = 0
        while right < len(s):
            r = s[right]
            chars[ord(r)] += 1

            while chars[ord(r)] > 1:
                l = s[left]
                chars[ord(l)] -= 1
                left += 1

            res = max(res, right - left + 1)

            right += 1
        return res


obj=Solution()
obj.lengthOfLongestSubstring('tmmzuxta')
