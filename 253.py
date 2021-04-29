class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        i = j = 0
        start = sorted(intervals, key=lambda x: x[0])
        end = sorted(intervals, key=lambda x: x[1])
        n = len(intervals)
        res = 0
        while i < n and j < n:
            if start[i][0] < end[j][1]:
                i += 1
                res += 1
            else:
                i += 1
                j += 1
        return res
        