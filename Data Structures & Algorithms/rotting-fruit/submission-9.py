class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        mins = 0
        fresh = 0
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
        while queue and fresh > 0:
            layer = len(queue) 
            for _ in range(layer):
                r,c = queue.popleft()
                #get all fresh surrounding fruit
                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c
                    if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] != 1:
                        continue
                    queue.append((nr,nc))
                    grid[nr][nc] = 2
                    fresh -= 1
            mins += 1

        return mins if fresh == 0 else -1