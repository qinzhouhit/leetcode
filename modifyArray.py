# -*- coding: utf-8 -*-


from heapq import heapify, heappop, heappush, heappushpop
from queue import PriorityQueue

def modifyArray(arr):

    def helper1(arr): # decreasing
        s1, diff = 0, 0
        q = []
        for i in range(len(arr)):
            tmp = 0
            cur = arr[i]
            if q: 
                tmp = q[0] # tmp is min now
                print (q, tmp)
            if q and tmp < cur: # cur is larger!
                diff = cur - tmp # make cur as small as tmp
                s1 += diff
                heappushpop(q, cur) # replace tmp with cur
            heappush(q, cur)
        return s1
    
    def helper2(arr): # increasing
        s1, diff = 0, 0
        q = []
        for i in range(len(arr)):
            tmp = 0
            cur = -arr[i]
            if q: 
                tmp = q[0] # tmp is min now
            if q and tmp < cur: # 
                diff = cur - tmp
                s1 += diff
                heappop(q)
                heappush(q, cur)
            heappush(q, cur) # for the 1st val
        return s1
    
    s1 = helper1(arr)
    s2 = helper2(arr)
    return min(s1, s2)
    

# print (modifyArray([0,1,2,5,6,2,7]))
# print (modifyArray([ 3, 1, 2, 1 ]))
print (modifyArray([ 9,8,7,1000,5,4,3,2,1 ]))