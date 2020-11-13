'''
keys: compare the 1st element of interval to the last element of last interval
Solutions:
Similar:
T: O(nlogn)
S: O(1)
'''
from typing import List
'''
Just go through the intervals sorted by start coordinate
and either combine the current interval with the previous one
if they overlap, or add it to the output by itself if they don't.
'''


''' 
Facebook Follow-Up
Question: How do you add intervals and merge them for a large stream of 
intervals? (Facebook Follow-up Question)
https://leetcode.com/problems/merge-intervals/solution/321556

'''

class Solution:
    
    def merge1(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        
        intervals.sort() # sort on 1st val, then 2nd
        print (intervals)
        res = []
        for interval in intervals:
            if res and interval[0] <= res[-1][-1]:
                res[-1][-1] = max(res[-1][-1], interval[1])
            else:
                res.append(interval)
        return res
    
    def merge(self, intervals):
        out=[]
        for i in sorted(intervals, key=lambda i:i[0]):
            if out and i[0] <= out[-1][-1]:
                out[-1][-1] = max(out[-1][-1], i[-1])
            else:
                out.append(i)
        return out
    
    
    

obj=Solution()
print(obj.merge([[1,3],[2,6],[8,10],[15,18]]))


