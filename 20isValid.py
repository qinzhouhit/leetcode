'''
keys: a dict of close: open brackets
Solutions:
Similar:
T:
S:
'''

class Solution:
    
    # O(N) for S and T
    def isValid2(self, s: str) -> bool:
        hashmap = {")": "(", "}": "{", "]":"["}
        stack = []
        for c in s:
            if c not in hashmap:
                stack.append(c)
            else:
                tmp = stack.pop() if stack else "#"
                if hashmap[c] != tmp:
                    return False
        
        return stack == []

    # self-made
    def isValid(self, s: str) -> bool:
        
        h = {"]": "[", "}": "{", ")": "("}
        
        stack = []
        for c in s:
            if c not in h:
                stack.append(c)
            elif not stack or h[c] != stack[-1]:
                return False # not stack meaing we directly have "]" coming
            else: # stack not [] and h[c] == stack[-1]
                stack.pop()
        return stack == []
    
    # concise; but O(N^2)
    def isValid1(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if n == 0:
            return True
        
        if n % 2 != 0:
            return False
            
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('{}','').replace('()','').replace('[]','')
        
        if s == '':
            return True
        else:
            return False
    
    # @return a boolean
    def isValid(self, s: str) -> bool:
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
