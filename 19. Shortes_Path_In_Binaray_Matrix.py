# -----------------------------------------------
# DESCRIPTION
# -----------------------------------------------
# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.

 

# Example 1:


# Input: grid = [[0,1],[1,0]]
# Output: 2
# Example 2:


# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4
# Example 3:

# Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
# Output: -1
 

# Constraints:

# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] is 0 or 1



# -------------------------------------------------------
# CODE TO PERFORM TASK
# -------------------------------------------------------
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)
        
        # Safety Check: If the start or end cell is blocked by a brick wall (1), stop!
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
            
        # Our queue tracks: (row, col, current_step_count)
        queue = deque([(0, 0, 1)])
        grid[0][0] = 1 # Mark it as wet/visited so we don't double-count it
        
        # The 8 movements the water can flow (Up, Down, Left, Right + 4 Diagonals)
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]
        
        while queue:
            # Serve the next wet cell at the front of the line
            r, c, steps = queue.popleft()
            
            # If this cell is the bottom-right corner, we win! Return the steps.
            if r == n - 1 and c == n - 1:
                return steps
                
            # Pour water into all 8 directions
            for dr, dc in directions:
                next_r, next_c = r + dr, c + dc
                
                # If the neighbor is inside the grid and is a clear path (0)
                if 0 <= next_r < n and 0 <= next_c < n and grid[next_r][next_c] == 0:
                    grid[next_r][next_c] = 1 # Make it wet
                    queue.append((next_r, next_c, steps + 1)) # Put it at the back of the line
                    
        # If the queue runs out of cells and water never hit the target corner, it's blocked.
        return -1
