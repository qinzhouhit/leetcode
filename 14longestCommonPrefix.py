'''
keys:
Solutions:
Similar:
T:
S:
'''


class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for str_ in strs:
                if str_[i]!=ch:
                    return shortest[:i]
        return shortest

        # if len(strs)==0: return ""
        # if len(strs)==1: return strs[0]
        # lens=[]
        # letters=[]; res=""
        # for i in range(min(lens)):
        #     for str_ in strs:
        #         letters.append(str_[i])
        #     if len(set(letters))==1:
        #         res+=letters[0]
        #         letters=[]
        #         continue
        #     else:
        #         return res
obj=Solution()
print(obj.longestCommonPrefix(["flower","flow","flight"]))
