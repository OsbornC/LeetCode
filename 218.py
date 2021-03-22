class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        ls = []
        res = [[0, 0]]
        heights = [[0, float("inf")]]
        last = [0, 0]
        for b in buildings:
            ls.append((b[0], -b[2], b[1]))
            ls.append((b[1], b[2], 0))
        ls.sort()
        for p in ls:
            while p[0] >= heights[0][1]:
                heapq.heappop(heights)
            if p[1] < 0:
                heapq.heappush(heights, [p[1], p[2]])
            if res[-1][1] != -heights[0][0]:
                res.append([p[0], -heights[0][0]])
        return res[1:]
        