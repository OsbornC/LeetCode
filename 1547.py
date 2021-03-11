class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        dp = [[float("inf")] * 102 for i in range(102)]
        def dfs(l, r, dp):
            if dp[l][r] != float("inf"):
                return dp[l][r]
            if l + 1 >= r:
                dp[l][r] = 0
                return 0
            for i in range(l+1, r):
                dp[l][r] = min(dp[l][r], dfs(l, i, dp) + dfs(i, r, dp) + cuts[r] - cuts[l])
            return dp[l][r] 
        cuts.append(0)
        cuts.append(n)
        cuts.sort()
        return dfs(0, len(cuts)-1, dp)