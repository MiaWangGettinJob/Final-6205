#Time complexity: O(m*n)
class Solution:
    def findway(self, grid):
        ROW, COL = len(grid), len(grid[0])
        if grid[0][0] == 1:
            return 0
        grid[0][0] = 1
        for i in range(1, ROW):
            if grid[i][0] == 0 and grid[i - 1][0] == 1:
                grid[i][0] = 1
            else:
                grid[i][0] = 0
        for j in range(1, COL):
            if grid[0][j] == 0 and grid[0][j - 1] == 1:
                grid[0][j] = 1
            else:
                grid[0][j] = 0

        for i in range(1, ROW):
            for j in range(1, COL):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                else:
                    grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

        return grid[-1][-1]

def main():
    a = Solution
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    print(a.findway(a,obstacleGrid))
    obstacleGrid = [[0,1],[0,0]]
    print(a.findway(a,obstacleGrid))

main()