'''
keys: a dict of close: open brackets
Solutions:
Similar:
T:
S:
'''

class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                # the order of two proposition matters
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []


obj=Solution()
print(obj.isValidParentheses1("]"))
