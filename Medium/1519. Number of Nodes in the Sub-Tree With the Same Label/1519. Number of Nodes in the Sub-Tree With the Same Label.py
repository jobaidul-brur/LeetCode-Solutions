class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # ETT
        time_stamp = 1
        start_time = [0] * n
        end_time = [0] * n
        csum = [[0] * 26 for _ in range(n + 1)]

        def dfs(node, parent):
            nonlocal time_stamp
            start_time[node] = time_stamp
            csum[time_stamp][ord(labels[node]) - ord('a')] = 1
            time_stamp += 1
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
            end_time[node] = time_stamp - 1

        dfs(0, -1)

        for i in range(1, n + 1):
            for j in range(26):
                csum[i][j] += csum[i - 1][j]

        ans = [0] * n
        for i in range(n):
            ans[i] = csum[end_time[i]][ord(labels[i]) - ord('a')] - csum[start_time[i] - 1][ord(labels[i]) - ord('a')]

        return ans
