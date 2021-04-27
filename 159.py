class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        res = 0
        dic = collections.defaultdict(int)
        n = len(s)
        l, r = 0, 0
        while r < n:
            dic[s[r]] += 1
            while len(dic.keys()) > 2 and l <= r:
                dic[s[l]] -= 1
                if dic[s[l]] == 0:
                    dic.pop(s[l])
                l += 1
            if len(dic.keys()) <= 2:
                res = max(res, r - l + 1)
            r += 1
        return res