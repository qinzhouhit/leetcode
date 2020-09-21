'''
keys: 2D Dp
Solutions:
Similar:
T: O(m*n), m and n as length of s and p
S: O(m*n)
'''
from typing import List

class Solution:
    # The DP table and the string s and p use the same indexes i and j, but
    # table[i][j] means the match status between p[:i] and s[:j], i.e.
    # table[0][0] means the match status of two empty strings, and
    # table[1][1] means the match status of p[0] and s[0]. Therefore, when
    # refering to the i-th and the j-th characters of p and s for updating
    # table[i][j], we use p[i - 1] and s[j - 1].

    def isMatch(self, s: str, p: str) -> bool:
        if not s or not p: return False
        m, n = len(s), len(p)

        # Initialize the table with False. The first row is satisfied.
        # dp[i][j] represents if the 0:i characters in s can match the 0:j characters in p
        dp = [[False] * (m+1)] * (n+1)

        # Update the corner case of matching two empty strings.
        dp[0][0] = True

        # Update the corner case of when s is an empty string but p is not.
        # Since each '*' can eliminate the charter before it, the table is
        # vertically updated by the one before previous. [test_symbol_0]
        for i in range(2, n + 1, 2):
            if p[i-1] == '*' and dp[0][i-2]:
                dp[0][i] = True

        # // Induction rule is very similar to edit distance, where we also consider from the end. And it is based on what character in the pattern we meet.
        # // 1. if p.charAt(j) == s.charAt(i), M[i][j] = M[i - 1][j - 1]
		# //    ######a(i)
		# //    ####a(j)
        # // 2. if p.charAt(j) == '.', M[i][j] = M[i - 1][j - 1]
        # // 	  #######a(i)
        # //    ####.(j)
        # // 3. if p.charAt(j) == '*':
        # //    1. if p.charAt(j - 1) != '.' && p.charAt(j - 1) != s.charAt(i), then b* is counted as empty. M[i][j] = M[i][j - 2]
        # //       #####a(i)
        # //       ####b*(j)
        # //    2.if p.charAt(j - 1) == '.' || p.charAt(j - 1) == s.charAt(i):
        # //       ######a(i)
        # //       ####.*(j)
		# //
		# // 	  	 #####a(i)
        # //    	 ###a*(j)
        # //      2.1 if p.charAt(j - 1) is counted as empty, then M[i][j] = M[i][j - 2]
        # //      2.2 if counted as one, then M[i][j] = M[i - 1][j - 2]
        # //      2.3 if counted as multiple, then M[i][j] = M[i - 1][j]
        #
		# // recap:
		# // M[i][j] = M[i - 1][j - 1]
		# // M[i][j] = M[i - 1][j - 1]
		# // M[i][j] = M[i][j - 2]
		# // M[i][j] = M[i][j - 2]
        # // M[i][j] = M[i - 1][j - 2]
        # // M[i][j] = M[i - 1][j]
		# // Observation: from above, we can see to get M[i][j], we need to know previous elements in M, i.e. we need to compute them first.
		# // which determines i goes from 1 to m - 1, j goes from 1 to n + 1

        for i in range(1, m+1):
            for j in range(1, n+1):
                curS = s[i-1]
                curP = p[j-1]
                if curS == curP or curP == ".":
                    dp[i][j] = dp[i-1][j-1]
                elif curP == "*":
                    preCurP = p[j-2]
                    if preCurP != "." and preCurP != curS: # a, b*
                        dp[i][j] = dp[i][j-2] # get rid of b* (b time 0), compare previous string
                    else: # matches, a, a* => 0 a, 1 a, or multiple a for p
                        # "a", "" or "a", "a" or "a", "aaaaa..."
                        # 0 a: so we compare s[:i] and p[:j-2]
                        # 1 a: so we compare s[:i] and p[:j-1]
                        # multiple a: so anything previous than "a" in s matches p
                        # addding this "a" won't change the matching
                        dp[i][j] = (dp[i][j-2] or dp[i][j-1] or dp[i-1][j])
        return dp[m][n]






    def isMatch1(self, s: str, p: str) -> bool:
        # The DP table and the string s and p use the same indexes i and j, but
        # table[i][j] means the match status between p[:i] and s[:j], i.e.
        # table[0][0] means the match status of two empty strings, and
        # table[1][1] means the match status of p[0] and s[0]. Therefore, when
        # refering to the i-th and the j-th characters of p and s for updating
        # table[i][j], we use p[i - 1] and s[j - 1].

        # Initialize the table with False. The first row is satisfied.
        table = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]

        # Update the corner case of matching two empty strings.
        table[0][0] = True

        # Update the corner case of when s is an empty string but p is not.
        # Since each '*' can eliminate the charter before it, the table is
        # vertically updated by the one before previous. [test_symbol_0]
        for i in range(2, len(p) + 1):
            table[i][0] = table[i - 2][0] and p[i - 1] == '*'

        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] != "*":
                    # Update the table by referring the diagonal element.
                    table[i][j] = table[i - 1][j - 1] and \
                                  (p[i - 1] == s[j - 1] or p[i - 1] == '.')
                else:
                    # Eliminations (referring to the vertical element)
                    # Either refer to the one before previous or the previous.
                    # I.e. * eliminate the previous or count the previous.
                    # [test_symbol_1]
                    table[i][j] = table[i - 2][j] or table[i - 1][j]

                    # Propagations (referring to the horizontal element)
                    # If p's previous one is equal to the current s, with
                    # helps of *, the status can be propagated from the left.
                    # [test_symbol_2]
                    if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                        table[i][j] |= table[i][j - 1]

        return table[-1][-1]



