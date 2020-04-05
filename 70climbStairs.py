'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
    def mySqrt(self, x):
        r=x
        while r*r>x:
            r=int((r+x/r)/2)
        return r

obj=Solution()
print(obj.mySqrt(10))


