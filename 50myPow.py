class Solution:
    # def myPow(self, x, n):
    #     if n==0:
    #         return 1
    #     if n>0:
    #         return x*self.myPow(x, n-1)
    #     if n<0:
    #         return self.myPow(1/x, -n)
    #     return self.myPow(x, n)

    def myPow(self, x, n):
        if n==0:
            return 1
        if n<0:
            return self.myPow(1/x, -n)
        if n%2:
            return x*self.myPow(x, n-1)
        return self.myPow(x*x, int(n/2))


obj=Solution()
print (obj.myPow(1.001, 123456))
