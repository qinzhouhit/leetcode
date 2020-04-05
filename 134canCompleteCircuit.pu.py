'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
    def canCompleteCircuit(self, gas, cost):
        start = 0
        tank = 0
        gasSum = 0
        costSum = 0
        for i in range(len(gas)):
            gasSum += gas[i]
            costSum += cost[i]
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0

        if gasSum < costSum:
            return -1
        else:
            return start

    def canCompleteCircuit1(self, gas, cost):
        total = 0 # determine if we have a solution
        for i in range(len(gas)):
            total += gas[i] - cost[i]
        if total < 0:
            return -1
        tank = 0; start = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0
        return start


obj = Solution()
print (obj.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
