class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        def test(cut):
            total = 0
            for i in range(n):
                if nums[i] % cut != 0:
                    total += nums[i] // cut + 1
                else:
                    total += nums[i] // cut
            return total <= threshold
        left, right = 1, max(nums)
        while left < right:
            mid = left + (right - left) // 2
            if test(mid):
                right = mid
            else:
                left = mid + 1
        return left