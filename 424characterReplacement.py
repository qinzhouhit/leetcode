'''keys: Solutions:Similar:T:S:'''from typing import List# https://leetcode.com/problems/longest-repeating-character-replacement/discuss/91271/Java-12-lines-O(n)-sliding-window-solution-with-explanationclass Solution:    # T: O(N); S: O(26)    def characterReplacement(self, s: str, k: int) -> int:        max_letter_ct = 0        h = {}        res = 0        l = 0        for r, c in enumerate(s):            if c not in h:                h[c] = 1            else:                h[c] += 1            max_letter_ct = max(max_letter_ct, h[c])                        # determine if it is a valid window            if r - l + 1 - max_letter_ct > k:                l_c = s[l]                h[l_c] -= 1                l += 1            res = max(res, r - l + 1)        return res                