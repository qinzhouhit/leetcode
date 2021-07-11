'''
keys: 
Solutions:
Similar:
T:
S:
'''



class Solution:
	# S and T: O(N)
	# reverse and flip upside down, if equal then true
    def isStrobogrammatic(self, num: str) -> bool:
        string_builder = []

        for c in  reversed(num):
            if c in {'0', '1', '8'}:
                string_builder.append(c)
            elif c == "6":
                string_builder.append("9")
            elif c == "9":
                string_builder.append("6")
            else:
                return False
        return num == "".join(string_builder)


    # concise version
    def isStrobogrammatic(self, num: str) -> bool:
        
        rotated_digits = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
        rotated_string_builder = []
        
        for c in reversed(num):
            if c not in rotated_digits:
                return False
            rotated_string_builder.append(rotated_digits[c])
        
        rotated_string = "".join(rotated_string_builder)
        return rotated_string == num


    # two pointer
    def isStrobogrammatic(self, num: str) -> bool:

    	digits_dict = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
    	l = 0
    	r = len(num) - 1
    	while l <= r:
    		if num[l] not in digits_dict or \
    			digits_dict[l] != num[r]:
    			return False
    		l += 1
    		r -= 1
    	return True
