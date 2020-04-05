'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
    def reverse(self, x: int) -> int:
        pos_neg=1
        if x<0:
            pos_neg=-1
            x=x*pos_neg
        N=len(str(x))
        new_str=''
        for i in range(N):
            new_str+=str(x)[N-1-i]
        rev_int=pos_neg*int(new_str)
        if rev_int<-2**31 or rev_int>2**31-1:
            return 0
        else:
            return rev_int

obj=Solution()
print(obj.reverse(1534236469))
