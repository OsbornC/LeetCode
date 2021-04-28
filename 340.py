class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        dic = collections.defaultdict(int)
        n = len(s)
        res = 0
        l, r = 0, 0
        while r < n:
            dic[s[r]] += 1
            while len(dic.keys()) > k:
                dic[s[l]] -= 1
                if dic[s[l]] == 0:
                    dic.pop(s[l])
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res
            