class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxsize = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        def dfs(r:int, c:int):
            if min(r,c) < 0 or r == rows or c == cols or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            cursize = 1
            cursize += dfs(r + 1, c)
            cursize += dfs(r - 1, c)
            cursize += dfs(r, c + 1)
            cursize += dfs(r, c - 1)
            return cursize
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxsize = max(dfs(r,c), maxsize)     
        return maxsize
                    