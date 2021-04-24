class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        ls = [0, 0, 0]
        l = 0
        res = 0
        for i in range(n):
            c = s[i]
            ls[ord(c) - ord('a')] += 1
            while ls[0] >= 1 and ls[1] >= 1 and ls[2] >= 1:
                ls[ord(s[l]) - ord('a')] -= 1
                l += 1
                res += n - i
        return res