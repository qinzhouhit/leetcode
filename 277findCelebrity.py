'''
keys:
Solutions:
Similar:
T:
S:
'''

"""
The knows API is already defined for you.
@param a, person a
@param b, person b
@return a boolean, whether a knows b
you can call Celebrity.knows(a, b)
"""
'''
The first for loop was to stop at a index which may be the celebrity.
Because that indexed person does not know any of the persons after it and some people before him may know him if candidate index is  >= 1 and 0 if it is the first person.
 You still need to check if that index is the correct one, so you check if any other person does not know him and if he knows any other person.
The answer is -1 or the candidate index.
However some may be confused if the potential candidate fails why cant there be any candidate indexes after it?
That is not possible because the potential candidate already does not know anyone after him which is the first step and before him are people who know atleast 1 person.
So there is no possibility of a celebrity in the right half.
'''

class Solution:
    # @param {int} n a party with n people
    # @return {int} the celebrity's label or -1
    def findCelebrity(self, n):
        candidate = 0

        for i in range(1, n):
            if knows(candidate, i):
                candidate = i # candidate can not be some index j after i...

        for i in range(n):
            if candidate != i and knows(candidate, i):
                return -1
            if candidate != i and not knows(i, candidate):
                return -1

        return candidate
