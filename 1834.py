class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        indices = list(range(n))
        indices.sort(key=lambda x: tasks[x][0])
        ans = list()
        q = list()
        timestamp = 0
        ptr = 0
        for i in range(n):
            if not q:
                timestamp = max(timestamp, tasks[indices[ptr]][0])
            while ptr < n and tasks[indices[ptr]][0] <= timestamp:
                heapq.heappush(q, (tasks[indices[ptr]][1], indices[ptr]))
                ptr += 1
            process, index = heapq.heappop(q)
            timestamp += process
            ans.append(index)
        return ans
                    