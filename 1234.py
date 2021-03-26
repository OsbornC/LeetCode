class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        m = n // 4
        dic = {
            "Q": 0,
            "W": 0,
            "E": 0,
            "R": 0
        }
        for i in range(n):
            dic[s[i]] += 1
        if dic['Q'] == m and dic['W'] == m and dic['E'] == m and dic['R'] == m:
            return 0
        l = 0
        res = n
        for r in range(n):
            dic[s[r]] -= 1
            while l <= r and dic['Q'] <= m and dic['W'] <= m and dic['E'] <= m and dic['R'] <= m:
                dic[s[l]] += 1
                res = min(res, r - l + 1)
                l += 1
        return res
        