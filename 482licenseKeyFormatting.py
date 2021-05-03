'''
keys: 
Solutions:
Similar: 
T:
S:
'''
from typing import List


class Solution:

    # some concise solution
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        S = S.replace("-", "").upper()[::-1]
        return '-'.join(S[i:i+K] for i in range(0, len(S), K))[::-1]


	# smart to use s1 = K if size % k == 0
	def licenseKeyFormatting(self, s: str, k: int) -> str:
		S = S.upper().replace('-','')
        size = len(S)
        ptr = K if size % K == 0 else size % K
        res = S[:ptr]
        while ptr < size:
            res += '-' + S[ptr: ptr+K]
            ptr += K
        return res


	# self-made
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        chars = [c.upper() for c in s if c != '-']
        if not chars:
            return ""
        
        remainder = len(chars) % k
        ct = k
        res = []
        
        res = chars[:remainder]
        rest = chars[remainder:]
        # print (res, rest)
        ptr = remainder
        while ptr < len(rest):
            # print (res)
            res.append('-')
            res += chars[ptr: ptr+k]
            ptr += k
        return "".join(res) if res[0] != '-' else "".join(res)[1:]       


