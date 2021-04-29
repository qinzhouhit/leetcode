'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
    # https://leetcode.com/problems/string-to-integer-atoi/discuss/4673/60ms-python-solution-OJ-says-this-beats-100-python-submissions
    def myAtoi(self, s: str) -> int:
        if len(s) == 0: 
            return 0
        # strip the leftmost and rightmost spaces
        s_list = list(s.strip()) # list will divide string into characters
        if not s_list: # s: " "
            return 0 
        pos_neg = -1 if s_list[0] == "-" else 1
        if s_list[0] in ["-", "+"]: 
            del s_list[0] # popleft()
        ret, i = 0, 0 # i as ptr
        while i < len(s_list) and s_list[i].isdigit():
            ret = ret*10 + ord(s_list[i]) - ord("0") # uss ord, int(s) takes more time
            i += 1
        return max(-2**31, min(pos_neg * ret, 2**31-1))

obj=Solution()
obj.myAtoi('     -42')
