class Solution:
    def __init__(self):
        self.res = 0
        self.empty = 1

    def dfs(self, grid, x, y, count):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == -1:
            return

        if grid[x][y] == 2:
            if self.empty == count:
                self.res += 1
            return

        grid[x][y] = -1

        self.dfs(grid, x + 1, y, count + 1)
        self.dfs(grid, x - 1, y, count + 1)
        self.dfs(grid, x, y + 1, count + 1)
        self.dfs(grid, x, y - 1, count + 1)

        grid[x][y] = 0

    def uniquePathsIII(self, grid):
        start_x, start_y = 0, 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    start_x, start_y = i, j
                elif grid[i][j] == 0:
                    self.empty += 1

        self.dfs(grid, start_x, start_y, 0)
        return self.res
