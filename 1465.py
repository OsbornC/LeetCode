class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts.insert(0, 0)
        verticalCuts.insert(0, 0)
        horizontalCuts.append(h)
        verticalCuts.append(w)
        width = 0
        height = 0
        for i in range(1, len(horizontalCuts)):
            width = max(width, horizontalCuts[i] - horizontalCuts[i-1])
        for j in range(1, len(verticalCuts)):
            height = max(height, verticalCuts[j] - verticalCuts[j-1])
        print(width, height)
        return int((width * height) % (10e9+7))
    