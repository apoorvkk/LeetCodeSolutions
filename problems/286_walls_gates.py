'''
URL: https://leetcode.com/problems/walls-and-gates
Time complexity: O(mn)
Space complexity: O(mn)
'''

from collections import deque

class Solution(object):
    def __init__(self):
        self.ROOM = 2**31 - 1
        self.GATE = 0

    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        queue = deque()
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == self.GATE:
                    queue.append((i,j))

        while len(queue) > 0:
            curr_x, curr_y = queue.popleft()

            self.get_next_neighbours(curr_x, curr_y, rooms, queue)

    def get_next_neighbours(self, x, y, rooms, queue):
        # look up
        if x - 1 >= 0 and rooms[x - 1][y] == self.ROOM:
            rooms[x - 1][y] = rooms[x][y] + 1
            queue.append((x - 1, y))
        # look down
        if x + 1 < len(rooms) and rooms[x + 1][y] == self.ROOM:
            rooms[x + 1][y] = rooms[x][y] + 1
            queue.append((x + 1, y))
        # look right
        if y + 1 < len(rooms[0]) and rooms[x][y+1] == self.ROOM:
            rooms[x][y+1] = rooms[x][y] + 1
            queue.append((x, y+1))
        # look left
        if y - 1 >= 0 and rooms[x][y-1] == self.ROOM:
            rooms[x][y-1] = rooms[x][y] + 1
            queue.append((x, y-1))
