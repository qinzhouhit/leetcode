'''keys: backtracking with trieSolutions:Similar: T:S:'''from typing import Listimport collections# >>> trie with class definitionclass TrieNode():    def __init__(self): # recursive definition        self.children = collections.defaultdict(TrieNode)        self.isWord = False    class Trie():    def __init__(self):        self.root = TrieNode()        def insert(self, word): # construct the trie        node = self.root        for letter in word:            node = node.children[letter]        node.isWord = True        # def search(self, word):    #     node = self.root    #     for w in word:    #         node = node.children.get(w)    #         if not node:    #             return False    #     return node.isWord    class Solution(object):    # S: O(N), N as the total number of letters in trie    # T: O(M(4*3^(L-1))), M as the number of cells in the board,    # L as the maximum length of words    def findWords(self, board, words):        res = [] # matched word                # construct the trie        trie = Trie()        node = trie.root        for w in words:            trie.insert(w)        for i in range(len(board)):            for j in range(len(board[0])):                self.dfs(board, node, i, j, "", res)        return res        def dfs(self, board, node, i, j, path, res):        if node.isWord:            res.append(path)            node.isWord = False        if not (0 <= i < len(board) and 0 <= j < len(board[0])):            return         tmp = board[i][j]        node = node.children.get(tmp)        if not node:            return         board[i][j] = "#"        self.dfs(board, node, i+1, j, path+tmp, res)        self.dfs(board, node, i-1, j, path+tmp, res)        self.dfs(board, node, i, j-1, path+tmp, res)        self.dfs(board, node, i, j+1, path+tmp, res)        board[i][j] = tmp# >>> trie # TLEdef findWords(self, board, words):    #make trie    trie = {}    for w in words:        t = trie        for c in w: # char            if c not in t:                t[c] = {}            t = t[c]        t['#']='#' # end of the word    self.res = set()    self.used = [[False] * len(board[0]) for _ in range(len(board))]    for i in range(len(board)):        for j in range(len(board[0])):            self.find(board, i, j, trie, '')    return list(self.res)    def find(self, board, i, j, trie, pre):    if '#' in trie:        self.res.add(pre)    if not (0 <= i < len(board) and 0 <= j < len(board[0])):        return    if not self.used[i][j] and board[i][j] in trie:        self.used[i][j] = True        self.find(board, i+1, j, trie[board[i][j]], pre+board[i][j])        self.find(board, i, j+1, trie[board[i][j]], pre+board[i][j])        self.find(board, i-1, j, trie[board[i][j]], pre+board[i][j])        self.find(board, i, j-1, trie[board[i][j]], pre+board[i][j])        self.used[i][j] = False