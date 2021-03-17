class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1: return 0
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        end = intervals[0][1]
        cnt = 1
        for interval in intervals[1:]:
            if interval[0] >= end:
                cnt += 1
                end = interval[1]
        return n - cnt