class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        visited = [False for _ in range(len(edges))]
        depth = {}
        ans = -1
        def dfs(node, d):
            nonlocal ans
            if visited[node]:
                return
            if node in depth:
                ans = max(ans, d - depth[node])
                return
            depth[node] = d
            if edges[node] != -1:
                dfs(edges[node], d + 1)

            visited[node] = True


        for i in range(len(edges)):
            dfs(i, 0)

        return ans
