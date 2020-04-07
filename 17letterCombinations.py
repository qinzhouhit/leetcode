'''
keys: recursion, layer by layer, e.g., ['a', 'b', 'c']. Then,
['ad', 'bd', 'cd']
Solutions:
Similar:
T: O(n*3^n)
S:
'''


# class Solution:
#     def letterCombinations(self, digits):
#         d2l={'2':"abc", '3':"der", '4':"ghi", \
#              '5':"jkl", '6':"mno", '7': "pqrs", \
#              '8':"tuv", '9':"wxyz"}
#         if len(digits)==0:
#             return []
#         if len(digits)==1:
#             return list(d2l[digits[0]])
#         prev = self.letterCombinations(digits[:-1])
#         additional = d2l[digits[-1]]
#         return [s + c for s in prev for c in additional]


# TODO: solution 2
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        interpret_digit = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': ' '}
        all_combinations = [''] if digits else []
        for digit in digits:
            current_combinations = list()
            for letter in interpret_digit[digit]:
                for combination in all_combinations:
                    current_combinations.append(combination + letter)
            all_combinations = current_combinations
        return all_combinations

obj=Solution()
print (obj.letterCombinations("23"))
