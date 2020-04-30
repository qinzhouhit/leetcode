'''
keys:
Solutions:
Similar:
T:
S:
'''

import collections
import heapq
class Solution:
    # T: O(NlogK), S: O(N)
    def kClosest(self, points, K):
        return heapq.nsmallest(K, points, lambda x: x[0] * x[0] + x[1] * x[1])

    # max heap
    # T: O(n), S: O(n)
    def kClosest2(self, points, K):
        q = [(x**2 + y**2, [x, y]) for x, y in points]
        heapq.heapify(q)
        return list(map(lambda x: x[1], heapq.nsmallest(K, q)))

    # T: O(nlogn), n as length of points
    # S: O(n)
    def kClosest1(self, points, K):
        points.sort(key=lambda P: P[0] ** 2 + P[1] ** 2)
        return points[:K]

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dict_ = collections.defaultdict(list)
        for pt in points:
            dict_[(pt[0], pt[1])] = self.distance(pt[0], pt[1])
        tmp = sorted(dict_.items(), key = lambda x: x[1])
        return list([v[0] for v in tmp[:K]])

    def distance(self, x, y):
        return x*x + y*y



obj = Solution()
print (obj.kClosest([[-5,4],[-6,-5],[4,6]], 2))
