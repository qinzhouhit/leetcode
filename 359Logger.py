'''keys: Solutions:Similar: T:S:'''from typing import Listfrom collections import defaultdictclass Logger:    # T: O(1), S: O(M), M as the size of all incoming messages    def __init__(self):        """        Initialize your data structure here.        """        self.mes2time = defaultdict(int)            def shouldPrintMessage(self, timestamp: int, message: str) -> bool:        """        Returns true if the message should be printed in the given timestamp, otherwise returns false.        If this method returns false, the message will not be printed.        The timestamp is in seconds granularity.        """        if message not in self.mes2time:            self.mes2time[message] = timestamp            return True        else:            time_pre = self.mes2time[message]            if timestamp - time_pre >= 10:                self.mes2time[message] = timestamp                return True        return False# Your Logger object will be instantiated and called as such:# obj = Logger()# param_1 = obj.shouldPrintMessage(timestamp,message)