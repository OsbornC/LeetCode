class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stk = []
        for node in preorder.split(','):
            stk.append(node)
            while len(stk) >= 3 and stk[-1] == '#' and stk[-2] == '#' and stk[-3] != '#':
                stk.pop(), stk.pop(), stk.pop()
                stk.append('#')
        return len(stk) == 1 and stk.pop() == '#'