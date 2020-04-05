'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
    """
    @param words: a list of words
    @param word1: a string
    @param word2: a string
    @return: the shortest distance between word1 and word2 in the list
    """
    def shortestDistance(self, words, word1, word2):
        # Write your code here
        n = len(words)
        ind1, ind2 = n, n
        dis = n
        for i in range(n):
            if words[i] == word1:
                ind1 = i
                dis = min(dis, abs(ind1 - ind2))
            if words[i] == word2:
                ind2 = i
                dis = min(dis, abs(ind1 - ind2))
        return dis

obj = Solution()
print (obj.shortestDistance(["practice", "makes", \
                             "perfect", "coding", "makes"],"coding","practice"))
