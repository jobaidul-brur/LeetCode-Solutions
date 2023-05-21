class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = collections.deque()
        def dfs(r, c):
            if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                grid[r][c] = 2
                queue.append((r, c, 0))
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)
        
        def enqueue():
            for r in range(m):
                for c in range(n):
                    if grid[r][c] == 1:
                        dfs(r, c)
                        return
        
        enqueue()
        
        while queue:
            r, c, d = queue.popleft()
            for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                if 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc] == 1:
                        return d
                    elif grid[nr][nc] == 0:
                        grid[nr][nc] = 2
                        queue.append((nr, nc, d+1))
        
        return -1  
