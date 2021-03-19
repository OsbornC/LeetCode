class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        lcs = [[0] * m for i in range(n)]
        for i in range(n):
            for j in range(m):
                if (i == 0 or j == 0) and text1[i] == text2[j]:
                    lcs[i][j] = 1
                    continue
                if text1[i] == text2[j]:
                    lcs[i][j] = max(lcs[i-1][j-1] + 1, lcs[i][j])
                else:
                    lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
                    
        return lcs[n-1][m-1]
        