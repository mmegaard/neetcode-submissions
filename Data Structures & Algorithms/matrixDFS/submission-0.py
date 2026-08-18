class Solution:
    def dfs(self, grid, x,y, seen):
        rows, cols = len(grid), len(grid[0]) 
        if min(x,y) < 0 or x == cols or y == rows or (x,y) in seen or grid[y][x] == 1:
            return 0
        if x == cols - 1 and y == rows - 1:
            return 1
        seen.add((x,y))
        count = 0
        count += self.dfs(grid, x, y + 1, seen)
        count += self.dfs(grid, x, y - 1, seen)
        count += self.dfs(grid, x + 1, y, seen)
        count += self.dfs(grid, x - 1, y, seen)
        seen.remove((x,y))
        return count
    

    def countPaths(self, grid: List[List[int]]) -> int:
        seen = set()
        return self.dfs(grid,0,0, seen)
    