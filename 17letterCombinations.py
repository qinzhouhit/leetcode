class Solution:
    def letterCombinations(self, digits):
        d2l={'2':"abc", '3':"der", '4':"ghi", \
             '5':"jkl", '6':"mno", '7': "pqrs", \
             '8':"tuv", '9':"wxyz"}
        if len(digits)==0:
            return []
        if len(digits)==1:
            return list(d2l[digits[0]])
        prev = self.letterCombinations(digits[:-1])
        additional = d2l[digits[-1]]
        return [s + c for s in prev for c in additional]

obj=Solution()
print (obj.letterCombinations("23"))
