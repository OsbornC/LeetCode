class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        n = len(s)
        pos = [-1] * (1 << 5)
        res, status = 0, 0
        pos[0] = 0
        for i in range(n):
            ch = s[i]
            if ch == 'a':
                status ^= 1<<0
            elif ch == 'e':
                status ^= 1<<1
            elif ch == 'i':
                status ^= 1<<2
            elif ch == 'o':
                status ^= 1<<3
            elif ch == 'u':
                status ^= 1<<4
            if (~pos[status]):
                res = max(res, i + 1 - pos[status])
            else:
                pos[status] = i + 1
        return res