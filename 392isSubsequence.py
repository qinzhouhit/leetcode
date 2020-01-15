class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: return True
        ind_s = 0; ind_t = 0
        while ind_t < len(t):
            if t[ind_t] == s[ind_s]:
                ind_s += 1
                if ind_s == len(s):
                    return True
            ind_t += 1
        return False
