class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        available = zip(capital, profits)
        available = sorted(available, key=lambda x: x[0])
        pos = 0
        n = len(profits)
        max_heap = []
        for _ in range(k):
            while pos < n and available[pos][0] <= w:
                heapq.heappush(max_heap, -available[pos][1])
                pos += 1
            if max_heap:
                w += -heapq.heappop(max_heap)
            else:
                break
        return w
