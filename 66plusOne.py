'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
    def plusOne(self, digits):
        len_=len(digits)
        for i in reversed(range(0,len_)):
            if digits[i]<9:
                digits[i]+=1
                return digits
            digits[i]=0

        # new_=[0]*(len_+1)
        # new_[0]=1
        # return new_

obj=Solution()
print(obj.plusOne([9,9]))


# class Solution:
#     def plusOne(self, digits):
#         num=''
#         for d in digits:
#             num+=str(d)
#         new=str(int(num)+1)
#         res=[]
#         for c in new:
#             res.append(int(c))
#         return res
