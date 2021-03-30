'''keys: it won't go on indefinitely, there are actually only a few numbers can be reachedSolutions: circle detectionSimilar: T:S:'''from typing import Listclass Solution:    # official circle detection, hashmap    # T and S: O(logn), the number of digits in a number is given by logn     # S for the hashmap    def isHappy(self, n: int) -> bool:                def get_next(n):            total_sum = 0            while n > 0:                n, digit = divmod(n, 10)                total_sum += digit ** 2            return total_sum            seen = set()        while n != 1 and n not in seen:            seen.add(n)            n = get_next(n)        return n == 1            # two pointers detection; T: O(logn), S: O(1)    def isHappy(self, n: int) -> bool:          def get_next(number):            total_sum = 0            while number > 0:                number, digit = divmod(number, 10)                total_sum += digit ** 2            return total_sum            slow_runner = n        fast_runner = get_next(n)        while fast_runner != 1 and slow_runner != fast_runner:            slow_runner = get_next(slow_runner)            fast_runner = get_next(get_next(fast_runner))        return fast_runner == 1    # self-implement, use hashmap to detect circle    # T and S: O(logn)    def isHappy(self, n: int) -> bool:        circle = set()        res = self.helper(n)        while res != 1 and res not in circle:            circle.add(res)            res = self.helper(res)        if res == 1:            return True        def helper(self, num):        digits = list(str(num))        return sum([int(v)*int(v) for v in digits])                    