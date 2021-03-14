class Solution:
    def strangePrinter(self, s: str) -> int:
        if not s: return 0
        n = len(s)
        dp = [[1] * n for i in range(n)]
        for i in range(1, n+1): #length
            for left in range(n-1): #start
                right = i + left - 1
                if right >= n: continue
                if s[left] == s[right]:
                    dp[left][right] = dp[left][right-1]
                    continue
                dp[left][right] = dp[left][right-1] + 1
                for k in range(left, right):
                    if s[k] == s[right]:
                        dp[left][right] = min(dp[left][right], dp[left][k-1] + dp[k][right])
        return dp[0][-1]