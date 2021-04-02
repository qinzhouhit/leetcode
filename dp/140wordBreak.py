'''keys: dpSolutions:Similar: T:S:'''from typing import Listfrom collections import defaultdict, Counterclass Solution:                ##############    # bottom-up    def wordBreak1(self, s: str, wordDict: List[str]) -> List[str]:        # quick check on the characters,        # otherwise it would exceed the time limit for certain test cases.        if set(Counter(s).keys()) > set(Counter("".join(wordDict)).keys()):            return []        wordSet = set(wordDict)         dp = [[]] * (len(s)+1)        dp[0] = [""]        for endIndex in range(1, len(s)+1):            sublist = []            # fill up the values in the dp array.            for startIndex in range(0, endIndex):                word = s[startIndex:endIndex]                if word in wordSet:                    for subsentence in dp[startIndex]:                        sublist.append((subsentence + ' ' + word).strip())            dp[endIndex] = sublist        return dp[len(s)]    ##############    '''    top-down: Let N be the length of the input string and     W be the number of words in the dictionary.    T: O(N^2 + 2^N + W),         2^N for number of solutions, solutions for each prefix double at each step        N^2 for building intermediate result, e.g., k steps to build sol for length-k prefix        W for the number of steps to build the wordset from dictionary    S: O(2^N * N + W)    '''    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:        wordSet = set(wordDict)        # table to map a string to its corresponding words break        # {string: [['word1', 'word2'...], ['word3', 'word4', ...]]}        memo = defaultdict(list)                def helper(s):            # return list of word lists            if not sub:                return [[]]                        if sub in memo:                return memo[sub]                        for i in range(1, len(sub)+1):                cur = sub[:i]                if cur in wordDict:                    for substr in helper(sub[i:]):                        memo[sub].append([cur] + substr)                                    return memo[sub]                helper(s)        return [" ".join(words) for words in memo[s]]    ##############    # top down    # https://leetcode.com/problems/word-break-ii/discuss/44311/Python-easy-to-understand-solution    def wordBreak2(self, s, wordDict):        """        Consider the input "aaaaaa", with wordDict = ["a", "aa", "aaa", "aaaa",         "aaaaa", "aaaaa"]. Every possible partition is a valid sentence, and         there are 2^n-1 such partitions.         """        def helper(s):            if s in memo:                return memo[s]            if not s:return []                        res = []            for word in wordDict:                if s.startswith(word):                    if len(word) == len(s):                        res.append(word)                    else:                        resElse = helper(s[len(word):])                        for item in resElse:                            item = word + " " + item                            res.append(item)            memo[s] = res            return res                memo = {}        wordDict = set(wordDict) # O(W), W as number of words        return helper(s) # # O(2^N) for the recursion, N = len(s)    # >>> self-made, works!    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:        @functools.lru_cache(maxsize=None)        def helper(start, path):            # print (idx)            if start == len(s):                res.append(path)            for end in range(start+1, len(s)+1):                if s[start:end] in wordDict:                    if not path: # avoid " " at the beginning                        helper(end, s[start:end])                     else:                        helper(end, path + " " + s[start:end])                res = []        wordDict = frozenset(wordDict)        helper(0, "")        return ressol = Solution()sol.wordBreak2("catsanddog", ["cat", "cats", "and", "sand", "dog"])