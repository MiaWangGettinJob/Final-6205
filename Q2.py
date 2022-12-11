#Time complexity: O(m*n)
class Solution:
    def countisland(self, grid):
        def helper(i, j):
            if i < 0 or i >= ROW or j < 0 or j >= COL or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            helper(i, j + 1)
            helper(i, j - 1)
            helper(i + 1, j)
            helper(i - 1, j)

        result = 0
        ROW, COL = len(grid), len(grid[0])
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == "1":
                    result += 1
                    helper(i,j)
        return result



def main():
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    a = Solution
    print(a.countisland(a, grid))

    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print(a.countisland(a, grid))



main()