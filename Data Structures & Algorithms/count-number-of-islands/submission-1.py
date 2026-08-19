class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0
        def dfs(r:int,c:int):
            if min(r,c) < 0 or r == rows or c == cols or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        for r in range(0,rows):
            for c in range(0,cols):
                if grid[r][c] == "0":
                    continue
                count +=1
                dfs(r,c)
        return count

            