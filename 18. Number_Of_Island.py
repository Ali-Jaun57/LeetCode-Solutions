# ------------------------------------------------
# DESCRIPTION
# ------------------------------------------------
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.




# ----------------------------------------------------------
# CODE TO PERFORM TASK
# ----------------------------------------------------------
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            print("0")
            return 0

        rows = len(grid)
        columns = len(grid[0])

        countislands = 0

        def countisland(r,c):
            if r<0 or r>=rows or c<0 or c>=columns: 
                return 

            if grid[r][c] == "0":
                return

            grid[r][c] = "0"

            countisland(r+1,c)
            countisland(r-1,c)
            countisland(r,c+1)
            countisland(r,c-1) 

        for x in range(rows):
            for y in range(columns):
                if grid[x][y] == "1":
                    countislands += 1
                    countisland(x,y)
        print(countislands)
        return countislands
