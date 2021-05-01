class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic: return ""
        l, r = 0, len(self.dic[key]) - 1
        idx = -1
        ans = -1
        while l <= r:
            mid = l + (r - l) // 2
            if self.dic[key][mid][1] <= timestamp:
                l = mid + 1
                ans = self.dic[key][mid][0]
            else:
                r = mid - 1
        return ans if ans != -1 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)