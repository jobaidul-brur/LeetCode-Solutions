class SnapshotArray:

    def __init__(self, length: int):
        self.snapshots = [[] for _ in range(length)]
        self.snap_id = 0
        self.changes = []


    def set(self, index: int, val: int) -> None:
        self.changes.append((index, val))


    def snap(self) -> int:
        for index, val in self.changes:
            self.snapshots[index].append((self.snap_id, val))
        self.snap_id += 1
        self.changes = []
        return self.snap_id - 1


    def get(self, index: int, snap_id: int) -> int:
        if not self.snapshots[index]:
            return 0
        i = bisect.bisect_right(self.snapshots[index], (snap_id, float('inf')))
        return self.snapshots[index][i - 1][1] if i else 0



# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
