'''
keys:
Solutions:
Similar:
T:
S:
'''

#class Solution:
#     def restoreIpAddresses(self, s):
#         res=[]
#         self.helper(res, "", s, 0)
#         return res
#     def helper(self, res, tmp, s, start):
#         if start==4:
#             if not s:
#                 res.append(tmp[:-1])
#             return
#
#         for i in range(1,4):
#             if i<=len(s):
#                 if i==1:
#                     self.helper(res, tmp+s[:i]+'.', s[i:], start+1)
#                 elif i==2 and s[0]!='0':
#                     self.helper(res, tmp+s[:i]+'.', s[i:], start+1)
#                 elif i==3 and s[0]!='0' and int(s[:3])<=255:
#                     self.helper(res, tmp+s[:i]+'.', s[i:], start+1)

class Solution:
    def restoreIpAddresses(self, s):
        len_=len(s); res=[]
        for i in range(1, min(4, len_-2)):
            for j in range(i+1, min(i+4, len_-1)):
                for k in range(j+1, min(j+4, len_)):
                    s1=s[0:i]; s2=s[i:j]
                    s3=s[j:k]; s4=s[k:len_]
                    if self.isValid(s1) and self.isValid(s2)\
                        and self.isValid(s3) and self.isValid(s4):
                        res.append(s1+'.'+s2+'.'+s3+'.'+s4)
        return res

    def isValid(self, sub):
        if len(sub)>3 or len(sub)==0 or \
                (sub[0]=="0" and len(sub)>1) or int(sub)>255:
            return False
        return True


obj=Solution()
print (obj.restoreIpAddresses("25525511135"))
