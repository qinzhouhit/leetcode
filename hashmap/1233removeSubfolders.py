'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
    '''
    >>> hashset
    https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/discuss/409028/JavaPython-3-3-methods-from-O(n-*-(logn-%2B-m-2))-to-O(n-*-m)-w-brief-explanation-and-analysis.
    Sort cost nlogn;
    Outer for loop run n times; inner for loop cost i in each iteration due to
    substring(0, i), that is, 2 + ... + m, which is O(m ^ 2).
    Time: O(n(logn + m ^ 2)), space: (n * m), where n = folder.length,
    m = average size of the strings in folder.

    Check if the floder's parent fold in HashSet before adding it into the HashSet.
    Note: the part before any / is a parent.
    '''
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key=lambda x: len(x)) # sort by length
        seen = set()
        for f in folder:
            for i in range(2, len(f)): # check parent
                if f[i] == '/' and f[:i] in seen: # f[i]=="/" is for case like ["/a/b/c","/a/b/ca","/a/b/d"]
                    break # goes to first for loop
            else: # goes here after finish inner for loop
                seen.add(f)
        return list(seen)



# >>> trie
# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/discuss/409028/JavaPython-3-3-methods-from-O(n-*-(logn-%2B-m-2))-to-O(n-*-m)-w-brief-explanation-and-analysis.
class TrieNode:
    def __init__(self):
        self.children = {} # dict
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True # node with last char
    
    def find(self): # travese the trie
        def dfs(direc, node): # direc: path
            if node.isEnd: # the first time it reaches end, i.e., shortest directory
                answer.append('/' + '/'.join(direc))
                return
            for char in node.children:
                dfs(direc + [char], node.children[char])
        
        answer = []
        dfs([], self.root)
        return answer


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for f in folder:
            f = f.split('/')[1:] # [0] is ""
            trie.insert(f)
        return trie.find()






sol = Solution()
print (sol.removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]))
