'''keys: Solutions:Similar: T:S:'''from typing import Listclass Solution:    # T: O(max(N1, N2)), length of nums1 and nums2    # S: O(max(N1, N2))    def addStrings(self, num1: str, num2: str) -> str:        res = []        carry = 0                l1, l2 = len(num1)-1, len(num2)-1        while l1 >=0 or l2 >= 0:            x1 = ord(num1[l1]) - ord('0') if l1 >= 0 else 0            x2 = ord(num2[l2]) - ord('0') if l2 >= 0 else 0            val = (x1 + x2 + carry) % 10            carry = (x1 + x2 + carry) // 10            res.append(val)            l1 -= 1            l2 -= 1        if carry:            res.append(carry)        return "".join(str(v) for v in res[::-1])        