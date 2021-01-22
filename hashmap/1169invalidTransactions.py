'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List
from collections import defaultdict

'''
notice that we have to compare all possible pairs transactions for one person
input: ["alice,20,800,mtv","alice,50,100,mtv","alice,51,100,frankfurt"]
output: ["alice,20,800,mtv","alice,50,100,mtv","alice,51,100,frankfurt"]
There could also be duplicate transactions...
'''


# https://leetcode.com/problems/invalid-transactions/discuss/367221/Python-Both-Optimized-O(nlogn)-and-Brute-Force-O(n2)-Solutions-with-Explanations
class Transaction:
    def __init__(self, name, time, amount, city):
        self.name = name
        self.time = int(time)
        self.amount = int(amount)
        self.city = city


class Solution:
	# O(nlogn), n as the number of total transactions


    def invalidTransactions(self, transactions):
    	# * is nice
        allTrans = [Transaction(*transaction.split(',')) for transaction in transactions]
        allTrans.sort(key=lambda t: t.time) # O(nlogn) time

        user2transIdx = defaultdict(list)
        for idx, transaction in enumerate(allTrans): # O(n) time
            user2transIdx[transaction.name].append(idx)

        res = []
        for name, transIdx in user2transIdx.items(): # O(n) time
            left = right = 0
            for idx in transIdx: # all time index of the user's transactions
                tran = allTrans[idx] # tran is for transaction object
                if tran.amount > 1000:
                    res.append(f"{tran.name},{tran.time},{tran.amount},{tran.city}")
                    continue
                while left <= len(transIdx)-2 and allTrans[transIdx[left]].time < tran.time - 60: # O(60) time
                    left += 1 # exclusive
                while right <= len(transIdx)-2 and allTrans[transIdx[right+1]].time <= tran.time + 60: # O(60) time
                    right += 1 # inclusive
                for i in range(left, right+1): # O(120) time
                    if allTrans[transIdx[i]].city != tran.city:
                        res.append(f"{tran.name},{tran.time},{tran.amount},{tran.city}")
                        break

        return res


class Solution:
	# does not work for duplicat transaction cases
	# ["alice,20,1220,mtv","alice,20,1220,mtv"]
	def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        
        transaction_name = collections.defaultdict(list)
        for transaction in transactions:
            vals = transaction.split(',')
            transaction_name[vals[0]].append(vals[1:])
            
        ans = set()
        for name, transaction in transaction_name.items():
            for record in transaction:
                time, amount, city = record
                if int(amount) > 1000:
                    ans.add(','.join([name,time,amount,city]))
                else:
                    for other in transaction:
                        o_time,o_amount,o_city = other
                        if o_city != city and abs(int(o_time)-int(time)) <= 60:
                            ans.add(','.join([name,time,amount,city]))
                            break
        return ans


    # the version did not consider users
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
    	res = set()
    	trans = [t.split(",") for t in transactions]
    	trans.sort(key=lambda x: int(x[1]))

    	for i in range(len(trans)):
    		t1 = trans[i]
    		if int(t1[2]) > 1000:
    			res.add(f"{t1[0]},{t1[1]},{t1[2]},{t1[3]}")
    		for j in range(i+1, len(trans)):
    			t2 = trans[j]
    			if t1[0] == t2[0] and int(t2[1]) - int(t1[0]) <= 60 and t2[3] != t1[3]:
    				res.add(f"{t1[0]},{t1[1]},{t1[2]},{t1[3]}")
    				res.add(f"{t2[0]},{t2[1]},{t2[2]},{t2[3]}")
    	return list(res)

