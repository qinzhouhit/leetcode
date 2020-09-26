'''
keys: count same number repetitions and append the count and
what was repeated when a different number was encountered and
that for each consecutive different-from-previous number in a sequence.
Solutions:
Similar:
T:
S:
'''


class Solution:
    # T: O(n*)
    def countAndSay(self, n):
        s = '1'
        for _ in range(n-1):
            digit, temp, count = s[0], '', 0
            for l in s: 
                if digit == l: # digit not change, ct += 1
                    count += 1
                else: # when the digit changes, ct = 1
                    temp += str(count)+digit
                    digit = l
                    count = 1
            temp += str(count)+digit
            s = temp
        return s


    def countAndSay1(self, n):
        s = '1'
        for i in range(n-1):
            count = 1
            temp = []
            for index in range(1, len(s)):
                if s[index] == s[index-1]:
                    count += 1
                else:
                    temp.append(str(count))
                    temp.append(s[index-1])
                    count = 1
            temp.append(str(count))
            temp.append(s[-1])
            s = ''.join(temp)
        return s

obj=Solution()
print (obj.test(4))
