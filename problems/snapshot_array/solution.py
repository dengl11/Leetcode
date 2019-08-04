from bisect import bisect_right
class SnapshotArray:

    def __init__(self, length: int):
        self.data = {i: [(-float('inf'), 0)] for i in range(length)}
        self.snaps = 0
        

    def set(self, index: int, val: int) -> None:
        if self.snaps == self.data[index][0]:
            self.data[index][-1][1] = val
        else:
            self.data[index].append((self.snaps, val))
        

    def snap(self) -> int:
        self.snaps += 1
        return self.snaps - 1
        

    def get(self, index: int, snap_id: int) -> int:
        pos = bisect_right(self.data[index], (snap_id, float('inf'))) - 1
        return self.data[index][pos][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)