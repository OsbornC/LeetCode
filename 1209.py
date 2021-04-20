class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        n = len(s)
        stk = []
        for c in s:
            if not stk or stk[-1][0] != c:
                stk.append([c, 1])
            elif stk[-1][1] + 1 < k:
                stk[-1][1] += 1
            else:
                stk.pop()
        res = ''
        for (c, l) in stk:
            res += c * l
        return res