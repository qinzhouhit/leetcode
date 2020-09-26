'''
keys: recursion, layer by layer, e.g., ['a', 'b', 'c']. Then,
['ad', 'bd', 'cd']
Solutions:
Similar:
T: O(n*3^n)
S:
'''

# TODO: solution 2
class Solution(object):
    # T: O(3^N * 4^M), N as the number of digits mapping to 3 letters
    # M as the number of digits mapping to 4 letters
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digit2letters = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz', 
            '0': ' '} # "0": " "
        all_combs = [''] if digits else []
        for digit in digits:
            cur_combs = []
            for letter in digit2letters[digit]:
                for comb in all_combs:
                    cur_combs.append(comb + letter)
            all_combs = cur_combs
        return all_combs
    
    
    # recursion
    def letterCombinations1(self, digits):
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
