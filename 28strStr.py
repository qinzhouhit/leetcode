'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
    # optimal: Rabin Karp, constant time slice
    # i.e., O(N) time complexity in the worst case
    # rolling hash
    def strStr2(self, haystack, needle):
        L, n = len(needle), len(haystack)
        if L > n:
            return -1
        
        # base value for the rolling hash function
        a = 26
        # modulus value for the rolling hash function to avoid overflow
        modulus = 2**31
        
        # lambda-function to convert character to integer
        h_to_int = lambda i : ord(haystack[i]) - ord('a')
        needle_to_int = lambda i : ord(needle[i]) - ord('a')
        
        # compute the hash of haystack[:L] and reference hash of needle[:L]
        h = ref_h = 0
        for i in range(L):
            h = (h * a + h_to_int(i)) % modulus
            ref_h = (ref_h * a + needle_to_int(i)) % modulus
        if h == ref_h: # if the initial hash values are the same
            return 0
              
        # const value to be used often : a**L % modulus
        aL = pow(a, L, modulus) # (a ** L) % modulus
        for start in range(1, n - L + 1): # the start is the start in haystack
            # compute rolling hash in O(1) 
            # h1 = (h_0*a - c_0*aL - c_(L+1))
            h = (h * a - h_to_int(start - 1) * aL + \
                 h_to_int(start + L - 1)) % modulus
            if h == ref_h:
                return start

        return -1


obj=Solution()
print (obj.strStr("", ""))



    
# self-made
def strStr(self, haystack, needle):
    if not needle:
        return 0
    if needle in haystack:
        for i in range(0,len(haystack)):
            if haystack[i:(i+len(needle))]==needle:
                return i
    else:
        return -1


# linear time slicing
# T: O(L*(N-L))); S: O(1)
def strStr1(self, haystack, needle):
    for i in range(len(haystack) - len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1



# OMG...
def strStr(self, haystack, needle):
    return haystack.find(needle)