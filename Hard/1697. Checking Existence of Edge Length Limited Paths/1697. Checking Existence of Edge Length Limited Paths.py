class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        size = [1] * n
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            x, y = find(x), find(y)
            if x == y:
                return False
            if size[x] < size[y]:
                x, y = y, x
            parent[y] = x
            size[x] += size[y]
            return True

        edgeList.sort(key=lambda x: x[2])
        for i in range(len(queries)):
            queries[i].append(i)

        ans = [False] * len(queries)
        for p, q, limit, i in sorted(queries, key=lambda x: x[2]):
            while edgeList and edgeList[0][2] < limit:
                union(*edgeList.pop(0)[:2])
            ans[i] = find(p) == find(q)

        return ans
