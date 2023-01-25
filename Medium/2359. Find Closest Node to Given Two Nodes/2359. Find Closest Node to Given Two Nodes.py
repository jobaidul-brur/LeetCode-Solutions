class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        dis1 = [float('inf')] * (len(edges) + 1)
        dis1[node1] = 0
        queue = deque([node1])
        visited = set([node1])
        while queue:
            node = queue.popleft()
            parent = edges[node]
            if parent != -1 and parent not in visited:
                dis1[parent] = dis1[node] + 1
                visited.add(parent)
                queue.append(parent)

        dis2 = [float('inf')] * (len(edges) + 1)
        dis2[node2] = 0
        queue = deque([node2])
        visited = set([node2])
        while queue:
            node = queue.popleft()
            parent = edges[node]
            if parent != -1 and parent not in visited:
                dis2[parent] = dis2[node] + 1
                visited.add(parent)
                queue.append(parent)

        min_dis = float('inf')
        res = -1
        for i in range(len(dis1)):
            if max(dis1[i], dis2[i]) < min_dis:
                min_dis = max(dis1[i], dis2[i])
                res = i

        return res
