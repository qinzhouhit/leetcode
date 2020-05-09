'''
keys: need some proof here for using just one-pass
Solutions:
Similar:
T:
S:
'''
from typing import List

class Solution:
    # TODO: a clear version based on
    # https://youtu.be/nTKdYm_5-ZY
    def canCompleteCircuit2(self, gas: List[int], cost: List[int]) -> int:
        start_ind = 0
        deficit = 0; sum_ = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            sum_ += diff

            if sum_ < 0:
                start_ind = i + 1
                deficit += sum_
                sum_ = 0

        return start_ind if sum_ + deficit >= 0 else -1


    # TODO: improved
    # T: O(N) one pass; S: O(1)
    def canCompleteCircuit1(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        total_tank, curr_tank = 0, 0
        starting_station = 0
        for i in range(n):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            # If one couldn't get here,
            if curr_tank < 0:
                # Pick up the next station as the starting one.
                starting_station = i + 1
                # Start with an empty tank.
                curr_tank = 0

        return starting_station if total_tank >= 0 else -1

    # O(n^2) TLE
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        res = -1
        for ind in range(len(gas)): # ind: starting ind
            ct = len(gas)
            cur_stat = ind
            cur_gas = 0
            for incre in range(len(gas)):
                cur_gas += gas[cur_stat%(len(gas))] - cost[cur_stat%(len(gas))]
                if cur_gas < 0:
                    break
                cur_stat += 1
                ct -= 1

            if ct == 0:
                res = ind
        return res


sol = Solution()
print (sol.canCompleteCircuit2([5,1,2,3,4],[4,4,1,5,1]))
