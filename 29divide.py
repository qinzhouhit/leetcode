class Solution:
    def divide(self, dividend, divisor):
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)

# class Solution:
#     def divide(self, dividend, divisor):
#         res=0
#         sign_= (dividend<0) is (divisor<0)
#         dividend=abs(dividend); divisor=abs(divisor)
#         while dividend>=divisor:
#             res+=1
#             dividend-=divisor
#         if not sign_:
#             res = 0 - res
#         return min(max(-2147483648, res), 2147483647)

obj=Solution()
print (obj.divide(16, -3))
