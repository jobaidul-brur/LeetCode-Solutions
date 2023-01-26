class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in flights:
            graph[u].append((v, w))

        queue = deque([(src, 0, 0)])
        dist = [float('inf')] * n
        dist[src] = 0
        while queue:
            node, cost, cnt = queue.popleft()
            # print("node: ", node, "cost: ", cost, "cnt: ", cnt)
            for v, w in graph[node]:
                if cost + w < dist[v] and cnt + 1 <= k + 1:
                    dist[v] = cost + w
                    queue.append((v, cost + w, cnt + 1))

        return dist[dst] if dist[dst] != float('inf') else -1
