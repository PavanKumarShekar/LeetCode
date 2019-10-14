class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        numOfIslands = 0
        for i in range (len(grid)):
            for j in range (len(grid[i])):
                if grid[i][j] == '1':
                    numOfIslands += self.dfs(grid, i, j)
        return numOfIslands
    
    def dfs(self, grid, i, j):
        if (i<0 or i>= len(grid) or j<0 or j>= len(grid[i]) or grid[i][j] =='0'):
            return 0
        grid[i][j]='0'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
        return 1
    
    
              