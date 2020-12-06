'''
URL: https://leetcode.com/problems/shortest-bridge/
Time complexity: O(mn)
Space complexity: O(mn)
'''

from collections import deque

class Solution:
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        if len(A) == 0:
            return -1

        ones_visited = set()

        islands = []

        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1 and (i,j) not in ones_visited:
                    islands.append(self._bfs_island(i, j, A, ones_visited))
        if len(islands) < 2:
            return -1

        return self._bfs_between_islands(islands[0], islands[1], A)

    def _bfs_between_islands(self, source, dest, A):
        visited = set()
        queue = deque([(pos, 0) for pos in source])
        dists = {}

        while queue:
            curr_pos, curr_dist = queue.popleft()
            x, y = curr_pos

            for next_pos in [(x-1, y), (x+1, y), (x, y-1), (x,y+1)]:
                next_x, next_y = next_pos
                if 0 <= next_x < len(A) and 0 <= next_y < len(A[0]):
                    if not A[next_x][next_y] and next_pos not in visited:
                        queue.append((next_pos, curr_dist+1))
                        visited.add(next_pos)
                        dists[next_pos] = curr_dist+1

        min_dist = float('inf')

        for pos in dest:
            x, y = pos
            for next_pos in [(x-1, y), (x+1, y), (x, y-1), (x,y+1)]:
                next_x, next_y = next_pos
                if 0 <= next_x < len(A) and 0 <= next_y < len(A[0]):
                    if not A[next_x][next_y] and next_pos in dists:
                        min_dist = min(min_dist, dists[next_pos])
        return min_dist


    def _bfs_island(self, x, y, A, visited):
        border_ones = set()
        queue = deque()
        queue.append((x, y))
        visited.add((x, y))

        while queue:
            curr_x, curr_y = queue.popleft()

            for next_pos in [(curr_x-1, curr_y), (curr_x+1, curr_y), (curr_x, curr_y-1), (curr_x,curr_y+1)]:
                next_x, next_y = next_pos
                if 0 <= next_x < len(A) and 0 <= next_y < len(A[0]):
                    if not A[next_x][next_y]:
                        border_ones.add((curr_x, curr_y))

                    if A[next_x][next_y] and next_pos not in visited:
                        visited.add(next_pos)
                        queue.append(next_pos)
                else:
                    border_ones.add((curr_x, curr_y))
        return border_ones

