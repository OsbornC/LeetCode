class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        i, j = k, k
        res = nums[k]
        minimal = nums[k]
        while i > 0 or j < len(nums) - 1:
            if i <= 0 or (j < len(nums) - 1 and nums[i-1] < nums[j+1]):
                minimal = min(minimal, nums[j+1])
                j += 1
            else:
                minimal = min(minimal, nums[i-1])
                i -= 1
            res = max(res, (j - i + 1) * minimal)
        return res