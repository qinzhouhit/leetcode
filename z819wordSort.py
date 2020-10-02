'''keys: Solutions:Similar:T:S:'''from typing import Listimport collectionsfrom functools import cmp_to_keyclass Solution:    """    @param alphabet: the new alphabet    @param words: the original string array    @return: the string array after sorting    """    def wordSort(self, alphabet, words):        # Write your code here        self.d = {}        v = 0        for ch in alphabet:            self.d[ch] = v            v += 1        return sorted(words, key = cmp_to_key(self.myCompare))    def myCompare(self, v1, v2):                len1, len2 = len(v1), len(v2)        if len1 < len2: return -self.myCompare(v2, v1)        # len2 is the smaller one        for i in range(len2):            ch1, ch2 = v1[i], v2[i]            if self.d[ch1] < self.d[ch2]: return -1            if self.d[ch1] > self.d[ch2]: return 1        if len1 == len2: # equal            return 0        else: # len1 > len2, v1 bigger            return 1