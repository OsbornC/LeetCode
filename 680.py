class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(direction):
            i, j = 0, len(s) - 1
            cnt = 0
            while i < j:
                if  s[i] != s[j]:
                    if cnt == 1:
                        return False
                    cnt = 1
                    if direction == 'right':
                        j -= 1
                        continue
                    if direction == 'left':
                        i += 1
                        continue
                i += 1
                j -= 1
            return True
        return helper('right') or helper('left')
                