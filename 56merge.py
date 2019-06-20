'''
Just go through the intervals sorted by start coordinate
and either combine the current interval with the previous one
if they overlap, or add it to the output by itself if they don't.
'''

class Solution:
    def merge(self, intervals):
        out=[]
        for i in sorted(intervals, key=lambda i:i[0]):
            if out and i[0]<=out[-1][-1]:
                out[-1][-1]=max(out[-1][-1], i[-1])
            else:
                out.append(i)
        return out

obj=Solution()
print(obj.merge([[1,3],[2,6],[8,10],[15,18]]))


