from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
            return -1

        visit = set()
        queue = deque()
        visit.add((0,0))
        queue.append((0,0))
        length = 0
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                if rows - 1 == r and cols - 1 == c:
                    return length
                
                directions = [[1, 0], [0, 1], [0, -1], [-1, 0]]
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if min(nr, nc) < 0 or nr == rows or nc == cols or (nr,nc) in visit or grid[nr][nc] == 1:
                        continue
                    visit.add((nr,nc))
                    queue.append((nr,nc))

            length += 1
        return -1