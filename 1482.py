class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay): return -1
        left, right = min(bloomDay), max(bloomDay)
        n = len(bloomDay)
        def test(cut):
            lastIdx = 0
            bouquets = 0
            isInFlowers = bloomDay[0] >= cut
            l, r = 0, 0
            while r < n:
                if bloomDay[r] > cut:
                    if bloomDay[l] <= cut:
                        bouquets += (r - l) // k
                    l = r
                else:
                    if bloomDay[l] > cut:
                        l = r
                r += 1
            if bloomDay[r-1] <= cut:
                bouquets += (r - l) // k
            return bouquets >= m
        while left < right:
            mid = left + (right - left) // 2
            enough = test(mid)
            if enough:
                right = mid
            else:
                left = mid + 1
        return left
            