'''
URL: https://leetcode.com/problems/shortest-distance-from-all-buildings/
Time complexity: O(m^2*n^2)
Space complexity: O(m*n)
'''

from collections import deque

class Solution:
    def _bfs(self, i, j, grid, dists, num_connected_buildings, total_buildings):
        visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        queue = deque()

        queue.append((i, j, 0))
        visited[i][j] = True
        total_neighbour_buildings = 1
        while len(queue) > 0:
            x, y, dist = queue.popleft()

            for pos in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
                if (0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])) and not visited[pos[0]][pos[1]]:
                    visited[pos[0]][pos[1]] = True

                    if grid[pos[0]][pos[1]] == 1:
                        total_neighbour_buildings += 1
                    elif grid[pos[0]][pos[1]] == 0:
                        dists[pos[0]][pos[1]] += dist + 1
                        num_connected_buildings[pos[0]][pos[1]] += 1
                        queue.append((pos[0], pos[1], dist+1))

        if total_buildings == total_neighbour_buildings:
            return True
        return False

    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        num_connected_buildings = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        dists = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        total_buildings = sum(grid[i][j] for j in range(len(grid[0])) for i in range(len(grid)) if grid[i][j] == 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if not self._bfs(i, j, grid, dists, num_connected_buildings, total_buildings):
                        return -1

        return min([dists[i][j] for j in range(len(dists[0])) for i in range(len(dists)) if grid[i][j] == 0 and num_connected_buildings[i][j] == total_buildings] or [-1])


