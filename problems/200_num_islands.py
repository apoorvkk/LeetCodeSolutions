'''
URL: https://leetcode.com/problems/number-of-islands
Time complexity: O(m*n)
Space complexity: O(m*n)
'''

from collections import deque

class Solution(object):
    def _get_available_positions(self, i, j, grid, visited):
        available_positions = []
        if i - 1 >= 0 and not visited[i-1][j] and grid[i-1][j] == "1":
            available_positions.append((i-1, j))

        if i + 1 < len(grid) and not visited[i+1][j] and grid[i+1][j] == "1":
            available_positions.append((i+1, j))

        if j - 1 >= 0 and not visited[i][j-1] and grid[i][j-1] == "1":
            available_positions.append((i, j-1))

        if j + 1 < len(grid[0]) and not visited[i][j+1] and grid[i][j+1] == "1":
            available_positions.append((i, j+1))

        return available_positions

    def _bfs(self, i, j, grid, visited):
        queue = deque()
        visited[i][j] = True
        queue.append((i, j))

        while len(queue) > 0:
            i, j = queue.popleft()

            available_positions = self._get_available_positions(i, j, grid, visited)

            for pos in available_positions:
                visited[pos[0]][pos[1]] = True
                queue.append(pos)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        total_islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not visited[i][j]:
                    total_islands += 1
                    self._bfs(i, j, grid, visited)
        return total_islands
