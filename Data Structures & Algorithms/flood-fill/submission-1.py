class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        basecolor = image[sr][sc]
        if basecolor == color:
            return image
        rows,cols = len(image), len(image[0])

        def dfs(r: int, c: int):
            if min(r,c) < 0 or r == rows or c == cols or image[r][c] != basecolor :
                return
            image[r][c] = color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c- 1)

        dfs(sr,sc)
        return image