class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        X1, Y1, X2, Y2 = float("inf"), float("inf"), float("-inf"), float("-inf")
        points = set()
        area = 0
        for x1, y1, x2, y2 in rectangles:
            X1 = min(X1, x1)
            Y1 = min(Y1, y1)
            X2 = max(X2, x2)
            Y2 = max(Y2, y2)
            p1 = (x1, y1)
            p2 = (x1, y2)
            p3 = (x2, y1)
            p4 = (x2, y2)
            for p in [p1, p2, p3, p4]:
                if p in points:
                    points.remove(p)
                else:
                    points.add(p)
            area += (x2 - x1) * (y2 - y1)
        if area != (X2 - X1) * (Y2 - Y1):
            return False
        if len(points) != 4: return False
        if (X1, Y1) not in points: return False
        if (X1, Y2) not in points: return False
        if (X2, Y1) not in points: return False
        if (X2, Y2) not in points: return False
        return True