class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left, right = max(weights), sum(weights)
        n = len(weights)
        def canShip(capacity):
            days = 1
            curr = 0
            for i in range(n):
                curr += weights[i]
                if curr > capacity:
                    curr = weights[i]
                    days += 1   
            return days <= D
        while left < right:
            mid = left + (right - left) // 2
            if canShip(mid):
                right = mid
            else:
                left = mid + 1
        return left
            
        
        
        
        
        
        