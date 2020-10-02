'''
keys: digit level operation
Solutions:
Similar:
T:
S:
'''

class Solution:
    # https://leetcode.com/problems/multiply-strings/discuss/17605/Easiest-JAVA-Solution-with-Graph-Explanation
    # T: O(M*N); S: O(M+N)
    def multiply(self, num1, num2):
        res = [0]* (len(num1) + len(num2))
        for i, e1 in enumerate(reversed(num1)):
            for j, e2 in enumerate(reversed(num2)):
                # int1 = ord(v1) - ord('0')
                # int2 = ord(v2) - ord('0')
                res[i+j] += int(e1) * int(e2)
                res[i+j+1] += int(res[i+j] / 10) # carry
                res[i+j] %= 10
        # have 0 in the beginning
        while len(res) > 1 and res[-1] == 0: 
            res.pop()
        return ''.join( map(str,res[::-1]))

obj=Solution()
print(obj.multiply("15","6"))
