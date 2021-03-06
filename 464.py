class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False
        if maxChoosableInteger >= desiredTotal:
            return True
        dic = {}
        state = [0] * (maxChoosableInteger + 1)
        def backtrack(state, total, dic):
            key = str(state) 
            if key in dic: return dic[key]
            for i in range(1, len(state)):
                if state[i] == 0:
                    state[i] = 1
                    if total - i <= 0 or not backtrack(state, total - i, dic):
                        state[i] = 0
                        dic[key] = True
                        return True
                    state[i] = 0
            dic[key] = False
            return False
        
        return backtrack(state, desiredTotal, {})
                    