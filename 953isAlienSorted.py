'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_idx = {c: idx for idx, c in enumerate(order)}
        
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            
            # Find the first difference word1[k] != word2[k].   
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if order_idx[word1[j]] > order_idx[word2[j]]:
                        return False
                    break # if reach the end of min_len, then break, go to the next pair of words
            # If we didn't find a first difference, the
            # words are like ("app", "apple").
            else: # pay attention to the indent of this else
                if len(word1) > len(word2):
                    return False
        return True

    # dope one, replace the chars by idx in order
    # https://leetcode.com/problems/verifying-an-alien-dictionary/discuss/203185/JavaC%2B%2BPython-Mapping-to-Normal-Order
    def isAlienSorted1(self, words, order):
        m = {c: i for i, c in enumerate(order)}
        words = [[m[c] for c in w] for w in words]
        return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))



sol = Solution()
# print (sol.isAlienSorted(["apap","app"], "abcdefghijklmnopqrstuvwxyz"))
print (sol.isAlienSorted(["app","apple"], "abcdefghijklmnopqrstuvwxyz"))
