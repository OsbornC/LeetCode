class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        self.dic = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.list.append(val)
        if val not in self.dic:
            self.dic[val] = {len(self.list) - 1}
            return True
        else:
            self.dic[val].add(len(self.list) - 1)
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.dic: return False
        idx = self.dic[val].pop()
        if len(self.dic[val]) == 0: self.dic.pop(val)
        last_idx = len(self.list) - 1
        if last_idx != idx:
            self.list[idx] = self.list[last_idx]
            self.dic[self.list[idx]].remove(last_idx)
            self.dic[self.list[idx]].add(idx)
        self.list.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return choice(self.list)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()