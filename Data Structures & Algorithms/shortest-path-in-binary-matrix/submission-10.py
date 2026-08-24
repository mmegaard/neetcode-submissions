class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if grid[rows - 1][cols - 1] == 1 or grid[0][0] == 1:
            return -1
        queue = deque()
        queue.append((0,0, 1))
        grid[0][0] = 1
        directions = [[0,1],[0,-1],[1,0],[-1,0], [1, 1], [-1, -1], [1, -1], [-1,1]]
        while queue:
            r,c,l = queue.popleft()
            if r == rows - 1 and c == cols - 1:
                return l
            
            for dr, dc in directions:
                nr = dr + r
                nc = dc + c
                if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] == 1:
                    continue
                grid[nr][nc] = 1
                queue.append((nr,nc, l+1))
        return -1