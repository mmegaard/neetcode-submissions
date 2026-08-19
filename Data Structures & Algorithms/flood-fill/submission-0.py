class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        basecolor = image[sr][sc]
        rows,cols = len(image), len(image[0])
        seen = set()
        def dfs(r: int, c: int):
            if min(r,c) < 0 or r == rows or c == cols or image[r][c] != basecolor or (r,c) in seen:
                return
            image[r][c] = color
            seen.add((r,c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c- 1)

        dfs(sr,sc)
        return image