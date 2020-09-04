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
Because that indexed person does not know any of the persons after it and 
some people before him may know him if candidate index is  >= 1 and 0 if it 
is the first person.
 You still need to check if that index is the correct one, so you check if 
 any other person does not know him and if he knows any other person.
The answer is -1 or the candidate index.
However some may be confused if the potential candidate fails why cant there
 be any candidate indexes after it?
That is not possible because the potential candidate already does not know
 anyone after him which is the first step and before him are people who know
 atleast 1 person.
So there is no possibility of a celebrity in the right half.
'''

class Solution:
    # @param {int} n a party with n people
    # @return {int} the celebrity's label or -1
    def findCelebrity(self, n):
        candidate = 0

        '''
        suppose the candidate after the first for loop is person k, it means
        0 to k-1 cannot be the celebrity, because they know a previous or 
        current candidate. Also, since k knows no one between k+1 and n-1, 
        k+1 to n-1 can not be the celebrity either. Therefore, k is the only 
        possible celebrity, if there exists one.
        '''
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i # candidate can not be some index j after i...

        for i in range(n):
            if candidate != i and knows(candidate, i):
                return -1
            if candidate != i and not knows(i, candidate):
                return -1

        return candidate
    
    # T: O(n)
    def findCelebrity2(self, n: int) -> int:
        self.n = n
        celebrity_candidate = 0
        for i in range(1, n):
            if knows(celebrity_candidate, i):
                celebrity_candidate = i
        if self.is_celebrity(celebrity_candidate):
            return celebrity_candidate
        return -1

    def is_celebrity2(self, i):
        for j in range(self.n):
            if i == j: continue
            if knows(i, j) or not knows(j, i):
                return False
        return True
    
    # intuitive one; T: O(n^2), S: O(1)
    def findCelebrity1(self, n: int) -> int:
        self.n = n
        for i in range(n):
            if self.is_celebrity(i):
                return i
        return -1
    
    def is_celebrity1(self, i):
        for j in range(self.n):
            if i == j: continue # Don't ask if they know themselves.
            if knows(i, j) or not knows(j, i):
                return False
        return True
    
    
    
    
