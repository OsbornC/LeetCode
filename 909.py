class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        ans = 0
        
        def numToIdx(num, n):
            x = (num - 1) // n
            y = (num - 1) % n
            if x % 2 == 1:
                y = n - 1 - y
            x = n - 1 - x
            return [x, y]
            
        n = len(board)
        queue = [1]
        visited = set()
        while queue:
            sz = len(queue)
            for i in range(sz):
                node = queue.pop(0)
                if node == n * n:
                    return ans
                j = 1
                while j <= 6 and j + node <= n * n:
                    x, y = numToIdx(j + node, n)
                    nxt = 0
                    if board[x][y] == -1:
                        nxt = j + node
                    else:
                        nxt = board[x][y]
                    if nxt in visited:
                        j += 1
                        continue
                    visited.add(nxt)
                    queue.append(nxt)
                    j += 1
            ans += 1
        return -1
                
