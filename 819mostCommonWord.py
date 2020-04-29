'''
keys: regex
Solutions:
Similar:
T:
S:
'''


import re
import collections
class Solution:
    def mostCommonWord(self, paragraph, banned):
        banset = set(banned)
        ban = set(banned)
        # "w": a-z, A-Z, 0-9, _
        # "w+": This expression matches the alphanumeric character in the string
        # "r" for raw string
        words = re.findall(r'\w+', paragraph.lower())
        return collections.Counter(w for w in words if w not in ban).most_common(1)[0][0]

    def mostCommonWord1(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        for c in "!?',;.": paragraph = paragraph.replace(c, " ")
        d, res, count = {}, "", 0
        for word in paragraph.lower().split():
            if word in set(banned):
                continue
            elif word in d:
                d[word] += 1
            else:
                d[word] = 1
            if d[word] > count:
                count = d[word]
                res = word
        return res

obj = Solution()
obj.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
