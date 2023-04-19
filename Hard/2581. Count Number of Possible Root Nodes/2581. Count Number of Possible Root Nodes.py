class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        st = set()
        for i in range(len(guesses)):
            st.add((guesses[i][0], guesses[i][1]))

        graph = collections.defaultdict(list)
        for i in range(len(edges)):
            graph[edges[i][0]].append(edges[i][1])
            graph[edges[i][1]].append(edges[i][0])

        true_cnt = 0
        def dfs1(node, parent):
            nonlocal true_cnt
            for nei in graph[node]:
                if nei == parent:
                    continue
                dfs1(nei, node)
                if (node, nei) in st:
                    true_cnt += 1
        dfs1(0, -1)
        # print(true_cnt)
        ans = 0
        def dfs2(node, parent):
            nonlocal ans
            nonlocal true_cnt
            # print("Root: ", node, ": ", true_cnt)
            if true_cnt >= k:
                ans += 1

            for nei in graph[node]:
                if nei == parent:
                    continue
                if (node, nei) in st:
                    # print(f"Removing {node} -> {nei}")
                    true_cnt -= 1
                if (nei, node) in st:
                    # print(f"Adding {nei} -> {node}")
                    true_cnt += 1
                dfs2(nei, node)
                if (node, nei) in st:
                    true_cnt += 1
                if (nei, node) in st:
                    true_cnt -= 1
        dfs2(0, -1)
        return ans