class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        visited = set()
        def dfs(r,c,i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or (r,c) in visited or not board[r][c] == word[i]:
                return False

            visited.add((r,c))
            found = False
            for dr, dc in directions:
                result = dfs(dr + r, dc + c, i + 1)
                if result:
                    found = True
            visited.remove((r,c))
            return found
        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row,col, 0):
                    return True
        return False

