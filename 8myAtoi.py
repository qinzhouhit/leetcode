'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s)==0: return 0
        new_s=list(s.strip()) # list will divide string into characters
        pos_neg=-1 if new_s[0]=="-" else 1
        if new_s[0] in ["-","+"]: del new_s[0]
        ret, i = 0, 0
        while i < len(new_s) and new_s[i].isdigit():
            ret = ret*10 + ord(new_s[i]) - ord("0")
            i += 1
        return max(-2**31, min(pos_neg*ret, 2**31-1))

obj=Solution()
obj.myAtoi('     -42')
