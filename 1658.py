class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        l, r = 0, 0
        n = len(nums)
        curr = 0
        max_length = -float("inf")
        cnt = sum(nums) - x
        if cnt < 0: return -1
        while r < n:
            curr += nums[r]
            r += 1
            while curr > cnt and l <= r:
                curr -= nums[l]
                l += 1
            if curr == cnt:
                max_length = max(max_length, r - l)
        if max_length == -float("inf"): return -1
        return n - max_length