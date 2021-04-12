class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stk = []
        n = len(nums)
        max_del_cnt = n - k
        for i in range(n):
            while stk and stk[-1] > nums[i] and max_del_cnt:
                stk.pop()
                max_del_cnt -= 1
            stk.append(nums[i])
        return stk[:k]