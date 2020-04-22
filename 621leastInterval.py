'''
keys:
emptySlots = partCount * n
availableTasks = tasks.length - count(A)
idles = max(0, emptySlots - availableTasks)
result = tasks.length + idles
Solutions:
Similar:
T: O(n)
S: O(1)
'''
# https://leetcode.com/problems/task-scheduler/discuss/104500/Java-O(n)-time-O(1)-space-1-pass-no-sorting-solution-with-detailed-explanation

import collections
class Solution:
    def leastInterval(self, tasks, n: int):
        # get the maxCount of task
        counter = collections.defaultdict(int)
        max_ = 0; maxCount = 0
        for t in tasks:
            counter[t] += 1
            if max_ == counter[t]:
                maxCount += 1
            elif max_ < counter[t]:
                max_ = counter[t] # count(A), A: most frequent task
                maxCount = 1 # count of tasks with the same most frequency

        partCount = max_ - 1
        partLen = n - (maxCount - 1)
        emptySlots = partCount * partLen
        availableTasks = len(tasks) - max_ * maxCount
        idles = max(0, emptySlots - availableTasks)

        return len(tasks) + idles

obj=Solution()
print(obj.leastInterval(["A","A","A","B","B","B"], 2))



