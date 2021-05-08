class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if not arr: return False
        if arr[start] == 0: return True
        ls = [start]
        n = len(arr)
        visited = [False] * n
        visited[start] = True
        while ls:
            q = ls.pop(0)
            idx1 = q + arr[q]
            idx2 = q - arr[q]
            if idx1 < n and not visited[idx1]:
                if arr[idx1] == 0: return True
                ls.append(idx1)
                visited[idx1] = True
            if idx2 >= 0 and not visited[idx2]:
                if arr[idx2] == 0: return True
                ls.append(idx2)
                visited[idx2] = True
        return False
                