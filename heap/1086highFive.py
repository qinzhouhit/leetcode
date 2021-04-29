'''
keys: 
Solutions:
Similar: 
T:
S:
'''
from typing import List
import collections
from heapq import *

class Solution:
	# https://leetcode.com/problems/high-five/discuss/312443/Python-Sort-or-Priority-Queue-solution
	def highFive(self, items: List[List[int]]) -> List[List[int]]:
		items.sort(reverse=True) # sorting by ID, then scores, reversed
		res = []
		cur = []
		idx = items[0][0] # user id

		for i, val in items: # since we already sorted by id, we just
			if i == idx:
				if len(cur) < 5:
					cur.append(val)
			else:
				res.append([idx, sum(cur)//len(cur)])
				cur = [val]
				idx = i
		res.append([idx, sum(cur)//len(cur)])
		return res[::-1] # starting from small IDs

	### use heapq for each id
	def highFive(self, items: List[List[int]]) -> List[List[int]]:
		d = collections.defaultdict(list)

		for idx, val in items:
			heappush(d[idx], val)

			if len(d[idx]) > 5:
				heappop(d[idx])

		res = [[i, sum(d[i])//len(d[i])] for i in sorted(d)]
		return res



	### self-made, T: O(NlogN), S: O(N)
    from math import floor
    from collections import defaultdict
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        user2score = defaultdict(list)
        for user, score in items:
            user2score[user].append(score)
        
        user2onescore = defaultdict(int)
        for user, scores in user2score.items():
            scores.sort(reverse=True)
            user2onescore[user] = floor(sum(scores[:5])/5)
        
        
        return list(sorted(user2onescore.items(), key=lambda x:x[0]))
            
            