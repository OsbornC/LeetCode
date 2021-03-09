class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        memo = {}
        def willWin(curr, alice):
            if (curr, alice) in memo:
                return memo[curr, alice]
            if curr == 0:
                memo[curr, alice] = False
            root = int(math.sqrt(curr))
            if root * root == curr:
                memo[curr, alice] = True
            else:
                for i in range(1, root + 1):
                    if willWin(curr - i * i, not alice):
                        memo[curr, alice] = False
                    else:
                        memo[curr, alice] = True
                        break
            return memo[curr, alice]
        return willWin(n, True)