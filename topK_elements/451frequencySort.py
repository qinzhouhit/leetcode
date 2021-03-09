'''
keys: dict_.most_common() is interesting
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
	# multiset and bucket set
	# O(n) for S and T, n = len(s)
	def frequencySort2(self, s: str) -> str:
		if not s: return s

	    # Determine the frequency of each character.
	    counts = collections.Counter(s)
	    max_freq = max(counts.values())
	    
	    # Bucket sort the characters by frequency.
	    buckets = [[] for _ in range(max_freq + 1)]
	    for c, freq in counts.items():
	        buckets[freq].append(c)
	        
	    # Build up the string.
	    string_builder = []
	    # end idx is 1 since no letter with freq 0 will be recorded
	    # does not matter if end idx is -1
	    # for i in range(len(buckets) - 1, 0, -1): # -1 is fine, buckets[0] always empty
	    for i in range(max_freq, -1, -1):
	        for c in buckets[i]:
	            string_builder.append(c * i)
	            
	    return "".join(string_builder)


	# official, O(nlogn)
	def frequencySort1(self, s: str) -> str:
	    # Count up the occurances.
	    counts = collections.Counter(s)
	    
	    # Build up the string builder.
	    string_builder = []
	    for letter, freq in counts.most_common(): # sorting the tuple by frequence
	        # letter * freq makes freq copies of letter.
	        # e.g. "a" * 4 -> "aaaa"
	        string_builder.append(letter * freq)
	    return "".join(string_builder)



	# self-made
	# T: O(D*logD) where ‘D’ is the number of distinct characters in the input 
	# string. Worst case we have O(N*logN)
    # S: O(N), N as the length of string
    def frequencySort(self, s: str) -> str:
        ct = Counter(s)
        ct = sorted(ct.items(), key=lambda x: x[1], reverse=True)
        
        tmp = []
        for c, freq in ct:
            tmp.append(c*freq)
        return "".join(tmp)

    def frequencySort(self, s: str) -> str:
        ct = Counter(s)
        h = []
        for c, freq in ct.items():
            heapq.heappush(h, (-freq, c))
        res = ""
        while h:
            freq, c = heappop(h)
            res += c*(-freq)
        return res



        