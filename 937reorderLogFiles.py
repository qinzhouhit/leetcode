'''
keys: sort, lambda
Solutions:
Similar:
T:
S:
'''


class Solution:
    # https://leetcode.com/problems/reorder-data-in-log-files/discuss/198197/simple-Python3-solution-beats-99
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        digits = []
        letters = []
        # divide logs into two parts, one is digit logs, the other is letter logs
        for log in logs:
            if log.split()[1].isdigit(): # default delimiter is " "
                digits.append(log)
            else:
                letters.append(log)

        letters.sort(key = lambda x: x.split()[0])     # when suffix is tie, sort by identifier
        letters.sort(key = lambda x: x.split()[1:])    # sort by suffix
        result = letters + digits                      # put digit logs after letter logs
        return result


    # T: O(NlogN), N as the total contents of logs
    # S: O(N)
    def reorderLogFiles1(self, logs):
        def f(log):
            id_, rest = log.split(" ", 1) # sth.split(" ", x) where x determines how many splitted substrings you need
            return (0, rest, id_) if rest[0].isalpha() else (1,)

        return sorted(logs, key = f)

obj = Solution()
print (obj.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))
