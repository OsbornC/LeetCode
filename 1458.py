class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        dp = [[0] * (n2) for i in range(n1)]
        dp[0][0] = nums1[0] * nums2[0]
        for i in range(1, n1):
            dp[i][0] = max(dp[i-1][0], nums1[i] * nums2[0])
        for j in range(1, n2):
            dp[0][j] = max(dp[0][j-1], nums1[0] * nums2[j])
        for i in range(1, n1):
            for j in range(1, n2):
                dp[i][j] = max(nums1[i] * nums2[j], dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + nums1[i] * nums2[j])
        return dp[n1-1][n2-1]