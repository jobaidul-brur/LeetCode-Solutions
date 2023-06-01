class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        if len(grid) == 1:
            return 1
        queue = [(0, 0, 1)]
        grid[0][0] = 1
        while queue:
            x, y, step = queue.pop(0)
            if x == len(grid) - 1 and y == len(grid) - 1:
                return step
            for i, j in [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]:
                if 0 <= i < len(grid) and 0 <= j < len(grid) and grid[i][j] == 0:
                    queue.append((i, j, step+1))
                    grid[i][j] = 1
        
        return -1            
                
