class Node:
    def __init__(self, cnt):
        self.next = None
        self.prev = None
        self.keySet = set()
        self.cnt = cnt

class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyCnt = {}
        self.cntKey = {}
        self.head = Node(float("inf"))
        self.tail = Node(float("-inf"))
        self.head.next = self.tail
        self.tail.prev = self.head

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key in self.keyCnt:
            self.changeKey(key, 1)
        else:
            self.keyCnt[key] = 1
            if self.head.next.cnt != 1:
                self.addNodeAfter(Node(1), self.head)
            self.head.next.keySet.add(key)
            self.cntKey[1] = self.head.next     

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key in self.keyCnt:
            if self.keyCnt[key] == 1:
                self.removeFromNode(self.cntKey[1], key)
                self.keyCnt.pop(key)
            else:
                self.changeKey(key, -1)
        

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        return "" if self.tail.prev == self.head else next(iter(self.tail.prev.keySet))

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        return "" if self.head.next == self.tail else next(iter(self.head.next.keySet))
    
    def removeFromNode(self, currNode, key):
        currNode.keySet.remove(key)
        if len(currNode.keySet) == 0:
            self.removeNodeFromList(currNode)
            self.cntKey.pop(currNode.cnt)
    
    def removeNodeFromList(self, currNode):
        currNode.prev.next = currNode.next
        currNode.next.prev = currNode.prev
        currNode.next = None
        currNode.prev = None

    def addNodeAfter(self, newNode, prevNode):
        newNode.prev = prevNode
        newNode.next = prevNode.next
        prevNode.next.prev = newNode
        prevNode.next = newNode
        
    def changeKey(self, key, offset):
        cnt = self.keyCnt[key]
        self.keyCnt[key] = cnt + offset
        currNode = self.cntKey[cnt]
        newNode = None
        if cnt + offset in self.cntKey:
            newNode = self.cntKey[cnt + offset]
        else:
            newNode = Node(cnt + offset)
            self.cntKey[cnt + offset] = newNode
            self.addNodeAfter(newNode, currNode if offset == 1 else currNode.prev)
        newNode.keySet.add(key)
        self.removeFromNode(currNode, key)
# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()