class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if grid[rows - 1][cols - 1] == 1 or grid[0][0] == 1:
            return -1
        queue = deque()
        visit = set()
        visit.add((0,0))
        queue.append((0,0))

        directions = [[0,1],[0,-1],[1,0],[-1,0], [1, 1], [-1, -1], [1, -1], [-1,1]]
        length = 1
        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                if r == rows - 1 and c == cols - 1:
                    return length
                visit.add((r,c))
                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c
                    if min(nr, nc) < 0 or nr == rows or nc == cols or (nr, nc) in visit or grid[nr][nc] == 1:
                        continue
                    queue.append((nr,nc))
            length += 1
        return -1