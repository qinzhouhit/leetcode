'''
keys:
Solutions:
Similar:
T:
S:
'''



class Solution:
    def generateParenthesis(self, n):
        def generate(p, left, right, parens=[]):
            if left:         generate(p + '(', left-1, right)
            if right > left: generate(p + ')', left, right-1)
            if not right:    parens += p, # comma for concatenating the whole string
            return parens
        return generate('', n, n)

obj=Solution()
print (obj.generateParenthesis(3))
