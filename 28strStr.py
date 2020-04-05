'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        if needle in haystack:
            for i in range(0,len(haystack)):
                if haystack[i:(i+len(needle))]==needle:
                    return i
        else:
            return -1


obj=Solution()
print (obj.strStr("", ""))


# OMG...
def strStr(self, haystack, needle):
    return haystack.find(needle)

# this is better
def strStr(self, haystack, needle):
    for i in range(len(haystack) - len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1
