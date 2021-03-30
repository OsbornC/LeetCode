class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left, right = max(nums), sum(nums)
        def test(curr):
            total = 0
            split = 1
            for num in nums:
                if total + num > curr:
                    total = num
                    split += 1
                else:
                    total += num
            return split > m
                
        while left < right:
            mid = left + (right - left) // 2
            moreThanM = test(mid)
            if moreThanM:
                left = mid + 1
            else:
                right = mid
        return left
        