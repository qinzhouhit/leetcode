'''
keys:
Solutions:
Similar:
T: O(n)
S: O(1)
'''
from typing import List

import collections
class Solution:
    # T: O(N); S: O(1)
    def leastInterval1(self, tasks: List[str], n: int) -> int:
        # frequencies of the tasks
        frequencies = [0] * 26
        for t in tasks:
            frequencies[ord(t) - ord('A')] += 1
        
        frequencies.sort()

        # max frequency
        f_max = frequencies.pop()
        idle_time = (f_max - 1) * n
        
        while frequencies and idle_time > 0:
            idle_time -= min(f_max - 1, frequencies.pop())
        idle_time = max(0, idle_time)

        return idle_time + len(tasks)
    
    
    # https://leetcode.com/problems/task-scheduler/discuss/104500/Java-O(n)-time-O(1)-space-1-pass-no-sorting-solution-with-detailed-explanation
    # emptySlots = partCount * n
    # availableTasks = tasks.length - count(A)
    # idles = max(0, emptySlots - availableTasks)
    # result = tasks.length + idles
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



