class UndergroundSystem:

    def __init__(self):
        self.startInfo = dict()
        self.table = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.startInfo[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startTime = self.startInfo[id][1]
        idx = (self.startInfo[id][0], stationName)
        rec = self.table.get(idx, (0, 0))
        self.table[idx] = (rec[0] + t - startTime, rec[1] + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        amt, time = self.table[(startStation, endStation)]
        return amt / time


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)