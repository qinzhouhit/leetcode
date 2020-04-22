'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
    # # failed since maximum recursion depth exceeded in comparison
    # def myPow(self, x, n):
    #     if n==0:
    #         return 1
    #     if n>0:
    #         return x*self.myPow(x, n-1)
    #     if n<0:
    #         return self.myPow(1/x, -n)
    #     return self.myPow(x, n)

    # Recursive
    def myPow(self, x, n):
        if n==0:
            return 1
        if n<0:
            return self.myPow(1/x, -n)
        if n%2:
            return x*self.myPow(x, n-1)
        return self.myPow(x*x, int(n/2))


class Solution:
    myPow = pow


class Solution:
    def myPow(self, x, n):
        return x ** n

# if n & 1 was same as: if n % 2
# n >> 1 was same as : n //= 2

# iterative
class Solution:
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1: # if n%2, i.e., odd number
                pow *= x
            x *= x # for even number
            n >>= 1 # n //=2
        return pow

obj=Solution()
print (obj.myPow(1.001, 123456))
