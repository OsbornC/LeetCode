class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        n = len(piles)
        left, right = 1, max(piles)
        def test(limit):
            hours = 0
            for i in range(n):
                if piles[i] % limit == 0:
                    hours += piles[i] // limit
                else:
                    hours += piles[i] // limit + 1
            return hours <= H
        while left < right:
            mid = left + (right - left) // 2
            enough = test(mid)
            if enough:
                right = mid
            else:
                left = mid + 1
        return left
        