'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List

import collections
import heapq
class Solution:
    #######
    # T: O(NlogK), S: O(N)
    def kClosest(self, points, K):
        return heapq.nsmallest(K, points, lambda x: x[0] * x[0] + x[1] * x[1])

    #######
    # max heap
    # T: O(n), S: O(n)
    def kClosest2(self, points, K):
        q = [(x**2 + y**2, [x, y]) for x, y in points]
        heapq.heapify(q)
        return list(map(lambda x: x[1], heapq.nsmallest(K, q)))

    #######
    # T: O(nlogn), n as length of points
    # S: O(n)
    def kClosest1(self, points, K):
        points.sort(key=lambda P: P[0] ** 2 + P[1] ** 2)
        return points[:K]

    ####### not recommended
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dict_ = collections.defaultdict(list)
        for pt in points:
            dict_[(pt[0], pt[1])] = self.distance(pt[0], pt[1])
        tmp = sorted(dict_.items(), key = lambda x: x[1])
        return list([v[0] for v in tmp[:K]])

    def distance(self, x, y):
        return x*x + y*y

    ####### overload the comparison operator
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.distance2origin() > other.distance2origin()

    def distance2origin(self):
        return self.x * self.x + self.y * self.y

from heapq import *
def find_closest_points(points, K):
    maxHeap = []
    for i in range(K):
        heappush(maxHeap, points[i])
    for i in range(K, len(points)):
        if points[i].distance2origin() < maxHeap[0].distance2origin():
            heappushpop(maxHeap, points[i])
    return list(maxHeap)
print (find_closest_points([Point(-5,4),Point(-6,-5),Point(4,6)], 2))


# obj = Solution()
# print (obj.kClosest([[-5,4],[-6,-5],[4,6]], 2))



