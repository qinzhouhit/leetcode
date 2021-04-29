'''
keys:
Solutions:
Similar:
T:
S:
'''
import collections

class Solution:
    # T: O(NK), S: O(NK)
    def groupAnagrams1(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())
        
    
    # T: O(NKlogK), N as length of strs, K as max length of a string in strs
    def groupAnagrams(self, strs):
        groups = {}
        for s in strs:
            k = tuple(sorted(s))
            # print (k)
            groups[k] = groups.get(k, []) + [s]
        return list(groups.values())


obj=Solution()
print(obj.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
