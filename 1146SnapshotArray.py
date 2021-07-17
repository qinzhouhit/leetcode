""" 
keys: 
Solutions:
Similar:
T:
S:
"""

# https://leetcode.com/problems/snapshot-array/discuss/350562/JavaPython-Binary-Search


# https://leetcode.com/problems/snapshot-array/discuss/350639/Python-Dictionary
class SnapshotArray:

    def __init__(self, length: int):
        self.snaps = {i: {0: 0} for i in range(length)}
        self.snap_ct = 0
        

    def set(self, index: int, val: int) -> None:
        self.snaps[index][self.snap_ct] = val
        

    def snap(self) -> int:
        self.snap_ct += 1
        return self.snap_ct - 1

    # https://leetcode.com/problems/snapshot-array/discuss/350639/Python-Dictionary/647825
    def get(self, index: int, snap_id: int) -> int:
        # it will travel back to previous versions until a value 
        # for a requested index is found
        while snap_id > 0 and snap_id not in self.snaps[index]:
            snap_id -= 1
        return self.snaps[index][snap_id]


    # bianry version
    # https://leetcode.com/problems/snapshot-array/discuss/350639/Python-Dictionary/744203
    def get1(self, index: int, snap_id: int) -> int:
        if snap_id not in self.snaps[index]:
            keys_snaps = list(self.snaps[index].keys())
            idx = bisect.bisect(keys_snaps, snap_id)  # rightmost position to insert
            return self.snaps[index][keys_snaps[idx-1]]
        
        return self.snaps[index][snap_id]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)





