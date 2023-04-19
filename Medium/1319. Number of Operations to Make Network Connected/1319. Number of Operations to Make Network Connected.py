class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        link = [i for i in range(n)]
        size = [1] * n
        def find(x):
            if link[x] != x:
                link[x] = find(link[x])
            return link[x]
        def same(x, y):
            return find(x) == find(y)
        def unite(x, y):
            x, y = find(x), find(y)
            if x == y:
                return
            if size[x] < size[y]:
                x, y = y, x
            link[y] = x
            size[x] += size[y]

        extra_cables = 0
        for x, y in connections:
            if same(x, y):
                extra_cables += 1
            else:
                unite(x, y)

        components = 0
        for i in range(n):
            if find(i) == i:
                components += 1

        if components - 1 > extra_cables:
            return -1
        return components - 1