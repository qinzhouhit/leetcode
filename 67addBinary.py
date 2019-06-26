class Solution:
    def addBinary(self, a, b):
        res=[]
        la, lb=len(a)-1, len(b)-1; carry=0
        while la>=0 or lb>=0:
            sum=carry
            if lb>=0:
                sum+=int(b[lb])
                lb-=1
            if la>=0:
                sum+=int(a[la])
                la-=1
            res.append(sum%2)
            carry=int(sum/2)

        if carry!=0:
            res.append(carry)
        res.reverse()
        return ''.join(map(str, res))

obj=Solution()
print(obj.addBinary("1010", "1011"))
