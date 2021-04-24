class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        n = len(nums)
        res = 0
        cnt = 0
        while r < n:
            if nums[r] % 2 == 1:
                cnt += 1
            r += 1
            if cnt == k:
                tmp = r
                while r < n and nums[r] & 1 == 0:
                    r += 1
                rcnt = r - tmp
                lcnt = 0
                while nums[l] & 1 == 0:
                    l += 1
                    lcnt += 1
                res += (lcnt + 1) * (rcnt + 1)
                l += 1
                cnt -= 1
        return res