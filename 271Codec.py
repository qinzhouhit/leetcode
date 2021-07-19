""" 
keys: 
Solutions:
Similar:
T:
S:
"""


class Codec:

	# https://leetcode.com/problems/encode-and-decode-strings/solution/
	# use chunks with info pre-fix of 4-bytes chunk length string
	# integer size: 4 bytes, 4 * 8 bits
	def len_to_str(self, x):
		"""Encodes length of string to bytes string
		"""
		x = len(x)
		bytes_ = [chr(x >> (i * 8) & 0xff) for i in range(4)]
		bytes_.reverse()  # why
		bytes_str = "".join(bytes_)
		return bytes_str


	def encode(self, strs: [str]) -> str:
		"""encode here is a workaround to fix BE CodecDriver error
		:type strs: List[str]
        :rtype: str
        """
        return ''.join(self.len_to_str(x) + x.encode('utf-8') for x in strs)


    def str_to_int(self, bytes_str):
        """Decodes bytes string to integer.
        """
        result = 0
        for ch in bytes_str:
            result = result * 256 + ord(ch)
        return result


    def decode(self, s):
        """Decodes a single string to a list of strings.
        :type s: str
        :rtype: List[str]
        """
        i, n = 0, len(s)
        output = []
        while i < n:
            length = self.str_to_int(s[i: i + 4])
            i += 4
            output.append(s[i: i + length])
            i += length
        return output  



class Codec:
	# since strs[i] contains any possible characters out of 256 valid ASCII characters.
	# we can use non-ascii char as delimiter
	# T: O(N), S: O(1)
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        if len(strs) == 0:
            return chr(258)
        return chr(257).join(x for x in strs)



    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        if s == chr(258): 
            return []
        return s.split(chr(257))
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))