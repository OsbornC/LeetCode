class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            left = max(A[i][0], B[j][0])
            right = min(A[i][1], B[j][1])
            if left <= right:
                ans.append([left, right])
            if A[i][1] > B[j][1]:
                j += 1
            else:
                i += 1
        return ans
        