class Solution:
    def groupAnagrams(self, strs):
        groups={}
        for str_ in strs:
            k=tuple(sorted(str_))
            groups[k]=groups.get(k, [])+[str_]
        return list(groups.values())


obj=Solution()
print(obj.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
