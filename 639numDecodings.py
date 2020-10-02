'''keys: Solutions:Similar:T:S:'''from typing import List# general dp thoughts# https://leetcode.com/problems/decode-ways-ii/discuss/105258/Java-O(N)-by-General-Solution-for-all-DP-problems'''*: 9**: 15, (11-19, 21-26)*A: 2 (if 0 <= A <=6); or 1 (if A > 6)A*: 9 (if A == 1); or 6 (if A == 2); or 0'''class Solution:    # dp[i] --> number of all possible decode ways of s[0: i].    # dp[i] = C(s[i]) * dp[i-1] + C(s[i-1], s[i]) * dp[i-2]    # 2-value dp: dp[0]: dp[i-2]; dp[1]: dp[i-1]    # huahua; T: O(N), S: O(1); N as length of s    def numDecodings2(self, s: str) -> int:        # one character        def ways1(c):            if c == "0": return 0            if c == "*": return 9            return 1                def ways2(c1, c2):            if c1 == "*" and c2 == "*":                return 15            if c1 == "*": # c2 != "*"                if "0" <= c2 <= "6":                    return 2                else:                    return 1            elif c2 == "*": # c1 != "*"                if c1 == "1": # 11 -> 19                    return 9                elif c1 == "2": # 21 -> 26                    return 6                else: # 3x...                    return 0            else: # none of them is "*"                prefix = int(c1) * 10 + int(c2)                return 10 <= prefix <= 26 # 1                        if not s: return 0                kMod = 1000000007        dp = [1, ways1(s[0])] # dp[0] is empty string        for i in range(1, len(s)):            dp_i = ways1(s[i]) * dp[1] + ways2(s[i-1], s[i]) * dp[0]            dp_i %= kMod            dp[0] = dp[1]            dp[1] = dp_i        return dp[1]            # bottom up    def numDecodings1(self, s: str) -> int:        dp = [0] * (len(s)+1)        dp[0] = 1        if s[0] == "0":            return 0 # no way to parse "05"        dp[1] = 9 if s[0] == "*" else 1                for i in range(2, len(s)+1):            first = s[i-2]            second = s[i-1]            # for dp[i-1]            if second == "*": # 1-9                dp[i] += 9 * dp[i-1]            elif second > "0":                dp[i] += dp[i-1]            # dp[i-2]            if first == "*":                if second == "*":                    dp[i] += 15 * dp[i-2]                elif second <= "6":                    dp[i] += 2 * dp[i-2]                else:                    dp[i] += dp[i-2]            elif first == "1" or first == "2":                if second == "*":                    if first == "1":                        dp[i] += 9 * dp[i-2]                    else: # first == "2"                        dp[i] += 6 * dp[i-2]                elif int(first)*10 + int(second) <= 26:                    dp[i] += dp[i-2]                        dp[i] %= 10**9 + 7        return dp[len(s)]        # https://leetcode.com/problems/decode-ways-ii/discuss/105274/Python-Straightforward-with-Explanation    # e0 = current number of ways we could decode, ending on any number;    # e1 = current number of ways we could decode, ending on an open 1;    # e2 = current number of ways we could decode, ending on an open 2;    def numDecodings(self, s: str) -> int:        MOD = 10**9 + 7        e0, e1, e2 = 1, 0, 0        for c in s:            if c == '*':                f0 = 9*e0 + 9*e1 + 6*e2                f1 = e0                f2 = e0            else:                f0 = (c > '0') * e0 + e1 + (c <= '6') * e2                f1 = (c == '1') * e0                f2 = (c == '2') * e0            e0, e1, e2 = f0 % MOD, f1, f2        return e0        