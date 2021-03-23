class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        n = len(customers)
        satisfied = [0] * n
        total = 0
        for i in range(X):
            total += customers[i] if grumpy[i] == 1 else 0
        res = total
        
        for i in range(X, n):
            if grumpy[i] == 1:
                total += customers[i]
            if grumpy[i - X] == 1:
                total -= customers[i - X]
            if total > res:
                res = total
        sum_ = 0 
        for i in range(n):
            sum_ += customers[i] if grumpy[i] == 0 else 0
        return res + sum_