class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append((v))
            graph[v].append((u))

        edges = []
        st = set((u, v) for u, v in connections)
        cnt = 0
        def dfs(node, parent):
            nonlocal cnt
            if (parent, node) in st:
                cnt += 1
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)

        dfs(0, -1)
        return cnt