'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:

    def reverse(self, x: int) -> int:
        if x > 0:
            a = int( str(x)[::-1] )
        if x <= 0:
            a = -1 * int( str(-1 * x)[::-1] )
        minval = -2 ** 31
        maxval = 2 ** 31 - 1
        if a not in range(minval, maxval):
            return 0
        else:
            return a

    # even shorter
    def reverse(self, x: int) -> int:
        sign = [1,-1][x < 0]
        rst = sign * int(str(abs(x))[::-1])
        return rst if -(2**31)-1 < rst < 2**31 else 0

    # T: log(N), roughly log_10(x) digits in x
    # S: O(1)



    def reverse(self, x: int) -> int:
        pos_neg = 1
        if x < 0:
            pos_neg = -1
            x = x*pos_neg
        N = len(str(x))
        new_str = ''
        for i in range(N):
            new_str += str(x)[N-1-i]
        rev_int = pos_neg * int(new_str)
        if rev_int < -2**31 or rev_int > 2**31-1:
            return 0
        else:
            return rev_int

obj=Solution()
print(obj.reverse(1534236469))
