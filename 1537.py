class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        INF = 10 ** 9 + 7
        i, j = 0, 0
        n1, n2 = len(nums1), len(nums2)
        sum1, sum2 = 0, 0
        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                sum1 += nums1[i]
                i += 1
            elif nums2[j] < nums1[i]:
                sum2 += nums2[j]
                j += 1
            else:
                sum1 = sum2 = (max(sum1, sum2) + nums1[i]) % INF
                i += 1
                j += 1
        sum1, sum2 = sum1 + sum(nums1[i:]), sum2 + sum(nums2[j:])
        return max(sum1, sum2) % INF