'''keys: Solutions:Similar:T:S:'''from typing import Listclass Solution:    # dp[i]: total number of rewardable student records with i len    # https://www.youtube.com/watch?v=06YtJdBG0rk    # https://leetcode.com/problems/student-attendance-record-ii/discuss/101638/Simple-Java-O(n)-solution    def checkRecord1(self, n: int) -> int:        M = 1000000007        PorL = [0] * (n + 1) # ending with P or L, no A        P = [0] * (n + 1) # ending with P, no A        PorL[0] = P[0] = 1; PorL[1] = 2; P[1] = 1                for i in range(2, n+1):            # this line means ending with P, just appending P in PorL            # PP or PL            P[i] = PorL[i - 1]             # P[i] end with P; P[i-1] ends with one L (i.e., PL),             # P[i-2] end with two L (i.e., PLL).            PorL[i] = (P[i] + P[i-1] + P[i-2]) % M                    res = PorL[n]        # insert one A in the sequence        for i in range(n): # i: position of A            # len(i) + A + len(n-i-1)            s = (PorL[i] * PorL[n - i - 1]) % M            res = (res + s) % M                return res                # brute-force    # T: O(3^n); S: O(n^n)    M = 1000000007    ct = 0    def checkRecord(self, n: int) -> int:        self.generate("", n)        return self.ct        def generate(self, s, n):        if n == 0 and self.check(s):            self.ct = (self.ct+1) % self.M        elif n > 0:            self.generate(s + "A", n-1)            self.generate(s + "P", n-1)            self.generate(s + "L", n-1)        def check(self, s):        ct = 0        for c in s:            if ct < 2 and c == "A":                ct += 1        return s and ct < 2 and s.find("LLL") < 0                                 