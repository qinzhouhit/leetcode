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
        pow = 1
        while n:
            if n % 2: # if n & 1, i.e., odd number
                pow *= x
            x *= x # for even number, (x^2)^n
            n //= 2 # n >> 1
        return pow
    
    
    # Recursive
    def myPow(self, x, n):
        if n==0:
            return 1
        if n<0:
            return self.myPow(1/x, -n)
        if n%2:
            return x*self.myPow(x, n-1)
        return self.myPow(x*x, int(n/2))


    # don't use it
    myPow = pow


    # don't use it
    def myPow1(self, x, n):
        return x ** n


obj=Solution()
print (obj.myPow(1.001, 123456))
