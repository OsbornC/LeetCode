class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        memo = {}
        def dfs(l, r):
            if l+1 >= r:
                return 0
            if (l, r) in memo:
                return memo[l, r]
            res = float("inf")
            for k in range(l+1, r):
                res = min(res, dfs(l, k) + dfs(k, r) + values[l] * values[k] * values[r])
            memo[l, r] = res
            return memo[l, r]
        return dfs(0, len(values) - 1)
                