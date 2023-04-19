class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        visited = [False] * (n)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node):
            if visited[node]:
                return 0
            visited[node] = True
            return 1 + sum(dfs(child) for child in graph[node])

        ans = 0
        for i in range(0, n):
            if not visited[i]:
                tmp = dfs(i)
                ans += tmp * (n - tmp)
        return ans // 2