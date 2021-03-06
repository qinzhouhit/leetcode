 '''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List

'''
real-world issues: 
Data storage: store data in database to avoid data loss
Scalability: millions of users poer day. Using more than one computer 
to store the data. => concurrency
Other: fit with other code in the passenger-tracking system
Delete the checkin data after the checkout:
However, it would actually be better to delete the data. We don't need it 
(hence the reason it being overwritten isn't an issue), and in fact keeping 
it around will slowly increase the memory usage of the program over time
'''

class UndergroundSystem:

	# S: O(p+s^2), for p as maximum possible number of passengers making trips
	# s^2 for all the possible pairs of S stations in the trips
    def __init__(self):
    	self.check_in = {} # k: userId, v: [checkin stationName, t]
    	# notice how we make self-defined dict
        # k: (startstation, endstation): v: [cumulative time, number of trips]
    	self.trips = collections.defaultdict(lambda: [0, 0])

    # T: O(1)
    def checkIn(self, id: int, stationName: str, t: int) -> None:
    	self.check_in[id] = [stationName, t]

    # T: O(1)
    def checkOut(self, id: int, stationName: str, t: int) -> None:
    	start_station, start_t = self.check_in[id]
    	self.trips[(start_station, stationName)][0] += (t - start_t) # cumulative time
    	self.trips[(start_station, stationName)][1] += 1 # ct
    
    # T: O(1), so we need total time and number of trips
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, ct = self.trips[(startStation, endStation)]
        return totalTime / ct if ct else 0


class UndergroundSystem1:

	def __init__(self):
	    self.user = collections.defaultdict(list)
	    self.dest = collections.defaultdict(list)

	def checkIn(self, id, stationName, t):
	    self.user[id] = [stationName, t]

    # this will use more space since we append all the time intervals
	def checkOut(self, id, stationName, t):
	    start_station, prev_time = self.user[id]
	    self.dest[(start_station, stationName)].append(t-prev_time)

	def getAverageTime(self, startStation, endStation):
	    return float(sum(self.dest[(startStation,endStation)]))/len(self.dest[(startStation,endStation)])

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)





