class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[-1][-1]:
            return -1
        q = [(0, 0, 1)]
        grid[0][0] = 1
        for r, c, d in q:
            if r == c == n - 1:
                return d
            for nr in range(max(0, r - 1), min(n, r + 2)):
                for nc in range(max(0, c - 1), min(n, c + 2)):
                    if not grid[nr][nc]:
                        grid[nr][nc] = 1
                        q.append((nr, nc, d + 1))
        return -1