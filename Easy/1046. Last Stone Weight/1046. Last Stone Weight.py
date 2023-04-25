from queue import PriorityQueue


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = PriorityQueue()

        for stone in stones:
            pq.put(-stone)

        while pq.qsize() > 1:
            x = -pq.get()
            y = -pq.get()
            if x != y:
                pq.put(-(x - y))

        return -pq.get() if pq.qsize() == 1 else 0