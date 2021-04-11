class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        stk = []
        n = len(A)
        res = 0
        for i in range(n):
            if not stk or A[stk[-1]] > A[i]:
                stk.append(i)
        for i in range(n-1, -1, -1):
            while stk and A[stk[-1]] <= A[i]:
                res = max(res, i - stk.pop())
        return res