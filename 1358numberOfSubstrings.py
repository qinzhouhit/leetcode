'''keys: sliding windowSolutions:Similar:T:S:'''from typing import Listclass Solution:    # sliding window    # T: O(N); S: O(1)    def numberOfSubstrings(self, s: str) -> int:        res = i = 0        count = {c: 0 for c in 'abc'}                for j in range(len(s)):            count[s[j]] += 1            while all(count.values()): #                 count[s[i]] -= 1                i += 1            res += i        return res        sol = Solution()print (sol.numberOfSubstrings("abcabc"))