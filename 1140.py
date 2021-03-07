class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffixSum = [[0] * n for i in range(n)]
        suffixSum[-1] = piles[-1]
        for i in range(n-2, -1, -1):
            suffixSum[i] = suffixSum[i+1] + piles[i]
        memo = [[-1] * n for i in range(n)]
        def dfs(piles, i, M):
            if i == n: return 0
            if n - i <= 2 * M: return suffixSum[i]
            if memo[i][M] != -1: return memo[i][M]
            ans = 0
            for x in range(1, 2 * M + 1):
                ans = max(ans, suffixSum[i] - dfs(piles, i+x, max(x, M)))
            memo[i][M] = ans
            return memo[i][M]
        return dfs(piles, 0, 1)
        
            