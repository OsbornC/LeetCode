class CustomStack:

    def __init__(self, maxSize: int):
        self.stk = [0] * maxSize
        self.maxSize = maxSize
        self.idx = 0

    def push(self, x: int) -> None:
        if self.idx == self.maxSize: return
        self.stk[self.idx] = x
        self.idx += 1

    def pop(self) -> int:
        if self.idx == 0: return -1
        val = self.stk[self.idx - 1]
        self.stk[self.idx - 1] = 0
        self.idx -= 1
        return val

    def increment(self, k: int, val: int) -> None:
        m = min(k, self.idx)
        for i in range(m):
            self.stk[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)