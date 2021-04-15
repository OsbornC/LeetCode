class SnapshotArray:

    def __init__(self, length: int):
        self.ls = [{0: 0} for _ in range(length)]
        self.shot = 0

    def set(self, index: int, val: int) -> None:
        self.ls[index][self.shot] = val

    def snap(self) -> int:
        self.shot += 1
        return self.shot - 1

    def get(self, index: int, snap_id: int) -> int:
        dic = self.ls[index]
        if snap_id in dic: return dic[snap_id]
        k = list(dic.keys())
        i = bisect.bisect_left(k, snap_id)
        return dic[k[i-1]]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)