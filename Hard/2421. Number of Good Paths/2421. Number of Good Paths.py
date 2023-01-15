class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        link = [i for i in range(n)]
        size = [1] * n

        def find(x):
            if x != link[x]:
                link[x] = find(link[x])
            return link[x]

        def same(x, y):
            return find(x) == find(y)

        def union(x, y):
            x = find(x)
            y = find(y)
            if x == y:
                return
            if size[x] < size[y]:
                x, y = y, x
            link[y] = x
            size[x] += size[y]

        arr = defaultdict(list)
        for i in range(n):
            arr[vals[i]].append(i)

        ans = 0

        for val, nodes in sorted(arr.items()):
            for node in nodes:
                for nei in adj[node]:
                    if vals[nei] <= val:
                        union(node, nei)

            group = defaultdict(int)
            for node in nodes:
                group[find(node)] += 1

            for _, cnt in group.items():
                ans += cnt * (cnt + 1) // 2

        return ans
