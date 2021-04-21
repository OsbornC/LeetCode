class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        prefix = [0]
        for num in A:
            prefix.append(prefix[-1] + num)
        ans = 0
        cnt = collections.defaultdict(int)
        for x in prefix:
            ans += cnt[x]
            cnt[S + x] += 1
        return ans