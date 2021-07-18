""" 
keys: 
Solutions:
Similar:
T:
S:
"""


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
         s_list = list(s)
         for idx, source, target in zip(indices, sources, targets):
         	if not s[idx:].startswith(source):  # if not s.startswith(source, index)
				continue  # no need to change
			else:
				s_list[idx] = target
				for i in range(idx + 1, idx + len(source)):
					s_list[i] = ""  # just in case longer substr is switched to shorter substr
		return "".join(s_list)