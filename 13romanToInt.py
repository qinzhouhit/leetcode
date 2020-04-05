'''
keys:
Solutions:
Similar:
T:
S:
'''


class Solution:
    def romanToInt(self, s):
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        s2v={}
        for i in range(len(values)):
            s2v[numerals[i]]=values[i]
        sum_=0; i=0
        while i<=len(s)-1:
            if s[i:i+2] in s and s[i:i+2] in s2v:
                sum_+=s2v[s[i:i+2]]
                i+=2
            else:
                sum_+=s2v[s[i]]
                i+=1
        return sum_

    # else
    def romanToInt1(self, s):
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        z = 0
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                z -= roman[s[i]]
            else:
                z += roman[s[i]]
        return z + roman[s[-1]]

obj=Solution()
print(obj.romanToInt("III"))
