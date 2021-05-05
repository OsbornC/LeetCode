class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.curr = 0
        self.ls = []

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.ls.append(timestamp)
        self.curr = timestamp

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        target = timestamp - 300 + 1
        if target < 0:
            target = 0
        l, r = 0, len(self.ls)
        while l < r:
            mid = l + (r - l) // 2
            if self.ls[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return len(self.ls) - l


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)