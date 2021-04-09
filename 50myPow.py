'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
    # if n & 1 was same as: if n % 2
    # n >> 1 was same as : n //= 2
    # x^(2*n) = (x^2)^n
    # e.g., 5^6 = (5^2)^3 = 25^3 = (25*25)*(25)^1
    # iterative
    # T: log(n); S: O(1); since log(n) bits for integer n
    def myPow2(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        res = 1
        while n:
            if n % 2: # if n & 1, i.e., odd number
                res *= x
            x *= x # for even number, (x^2)^n
            n //= 2 # n >> 1
        return res


    # O(logN) recursion
    def myPow(self, x, n):

        def helper(x, n):
            if n == 0:
                return 1
            half = helper(x, n//2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x

        if n < 0:
            x = 1/x
            n = -n
        return helper(x, n)

    
    # Recursive
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            return self.myPow(1/x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, int(n/2))

    # another one, similar to the previous one
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            return self.myPow(1/x, -n)
        elif n % 2:
            return x*self.myPow(x*x, n//2)
        return self.myPow(x*x, n//2)


    # don't use it
    myPow = pow


    # don't use it
    def myPow1(self, x, n):
        return x ** n


obj=Solution()
print (obj.myPow(1.001, 123456))
