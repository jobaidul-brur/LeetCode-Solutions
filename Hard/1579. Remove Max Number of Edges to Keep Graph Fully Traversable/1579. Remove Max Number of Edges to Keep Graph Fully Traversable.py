class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.size = [1] * (n+1)
        self.count = n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.count -= 1
        return True

    def total_components(self):
        return self.count
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = DSU(n)
        bob = DSU(n)

        ans = 0
        for t, u, v in edges:
            if t == 3:
                if not alice.union(u, v):
                    ans += 1
                if not bob.union(u, v):
                    pass

        for t, u, v in edges:
            if t == 1:
                if not alice.union(u, v):
                    ans += 1
            elif t == 2:
                if not bob.union(u, v):
                    ans += 1

        if alice.total_components() != 1 or bob.total_components() != 1:
            return -1
        return ans
