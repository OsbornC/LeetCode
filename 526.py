class Solution:
    def countArrangement(self, n: int) -> int:
        self.ans = 0
        visited = set()
        def backtrack(path):
            if len(path) == n:
                self.ans += 1
                return
            for i in range(1, n+1):
                if i in visited: continue
                if i % (len(path) + 1) == 0 or (len(path) + 1) % i == 0:
                    
                    path.append(i)
                    visited.add(i)
                    backtrack(path)
                    visited.remove(i)
                    path.pop()
        backtrack([])
        return self.ans