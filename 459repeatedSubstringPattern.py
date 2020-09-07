'''keys: Solutions:Similar: T:S:'''from typing import Listimport reclass Solution:    # KMP, typically used for single pattern search    def repeatedSubstringPattern3(self, s: str) -> bool:        n = len(s)        dp = [0] * n # dp[i] -> the substring s[:(i+1)], the first i chars        # Construct partial match table (lookup table).        # It stores the length of the proper prefix that is also a proper suffix.        # ex. ababa --> [0, 0, 1, 2, 1]        # ab --> the length of common prefix / suffix = 0        # aba --> the length of common prefix / suffix = 1        # abab --> the length of common prefix / suffix = 2        # ababa --> the length of common prefix / suffix = 1        for i in range(1, n): # length of substring considered            j = dp[i - 1] #             while j > 0 and s[i] != s[j]:                j = dp[j - 1]            if s[i] == s[j]:                j += 1            dp[i] = j        l = dp[n - 1]        # check if it's repeated pattern string        return l != 0 and n % (n - l) == 0        ##### recommend    # easy to think of     def repeatedSubstringPattern0(self, s: str) -> bool:        n = len(s)                for i in range(n//2, 0, -1):            if n % i == 0:                num_repeats = n // i                sub_tmp = ""                sub = s[:i]                for j in range(num_repeats):                    sub_tmp += sub                if sub_tmp == s:                    return True        return False                # find divisors + rabin-karp, which is for multiple pattern search    # T: O(N*sqrt(N)); S: O(sqrt(N))    def repeatedSubstringPattern2(self, s: str) -> bool:        n = len(s)        if n < 2:            return False        if n == 2:            return s[0] == s[1]                # The length of the repeating substring must be a divisor of the         # length of the input string. Starting from n//2 or sqrt(n)        for i in range(int(n**0.5), 0, -1):            if n % i == 0:                divisors = [i]                if i != 1: # paired divisor                    divisors.append(n // i)                for d in divisors:                    first_hash = curr_hash = hash(s[:d])                    start = d                    while start != n and curr_hash == first_hash:                        curr_hash = hash(s[start:start + d])                        start += d # jumping                    if start == n and curr_hash == first_hash:                        return True                        return False            # T: O(N^2), S: O(N)    def repeatedSubstringPattern1(self, s: str) -> bool:        return s in (s + s)[1: -1]            # T: O(N^2), S: O(1)    def repeatedSubstringPattern(self, s: str) -> bool:        pattern = re.compile(r'^(.+)\1+$')        return pattern.match(s)        