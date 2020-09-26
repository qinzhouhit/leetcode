'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
    # O(max(N, M)) for S and T
    def addBinary(self, a, b):
        res = []
        la, lb = len(a)-1, len(b)-1; carry = 0
        while la >= 0 or lb >= 0:
            sum_ = carry
            if lb >= 0:
                sum_ += int(b[lb])
                lb -= 1
            if la >= 0:
                sum_ += int(a[la])
                la -= 1
            res.append(sum_ % 2)
            carry = sum_ // 2

        if carry != 0:
            res.append(carry)
        res.reverse()
        return ''.join(map(str, res))
    
    # T: O(N+M) for T, dont use it
    def addBinary1(self, a, b) -> str:
        return '{0:b}'.format(int(a, 2) + int(b, 2))
    
    

obj=Solution()
print(obj.addBinary("1010", "1011"))
