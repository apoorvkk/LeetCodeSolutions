'''
URL: https://leetcode.com/problems/spiral-matrix/
Time complexity: O(n*m)
Space complexity: O(1)
'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []

        num_visited_elems = 0
        width_size = len(matrix[0])
        height_size = len(matrix)
        spiral_ordered_elems = []
        ordered_directions = ["right", "down", "left", "up"]

        curr_direction = 0
        curr_pos_x = 0
        curr_pos_y = 0
        has_traversed_first_row = False

        while num_visited_elems < len(matrix[0]) * len(matrix):
            if ordered_directions[curr_direction] == "right":
                for i in range(width_size):
                    if i == 0 and has_traversed_first_row:
                        curr_pos_y += 1
                        continue

                    spiral_ordered_elems.append(matrix[curr_pos_x][curr_pos_y])
                    num_visited_elems += 1

                    if i != width_size - 1:
                        curr_pos_y += 1

                if has_traversed_first_row:
                    width_size -= 1
                else:
                    has_traversed_first_row = True

            elif ordered_directions[curr_direction] == "down":
                for i in range(height_size):
                    if i == 0:
                        curr_pos_x += 1
                        continue

                    spiral_ordered_elems.append(matrix[curr_pos_x][curr_pos_y])
                    num_visited_elems += 1

                    if i != height_size-1:
                        curr_pos_x += 1

                height_size -= 1

            elif ordered_directions[curr_direction] == "left":
                for i in range(width_size):
                    if i == 0:
                        curr_pos_y -= 1
                        continue

                    spiral_ordered_elems.append(matrix[curr_pos_x][curr_pos_y])
                    num_visited_elems += 1

                    if i != width_size - 1:
                        curr_pos_y -= 1


                width_size -= 1

            elif ordered_directions[curr_direction] == "up":
                for i in range(height_size):
                    if i == 0:
                        curr_pos_x -= 1
                        continue

                    spiral_ordered_elems.append(matrix[curr_pos_x][curr_pos_y])
                    num_visited_elems += 1

                    if i != height_size - 1:
                        curr_pos_x -= 1

                height_size -= 1

            curr_direction = (curr_direction + 1) % len(ordered_directions)
        return spiral_ordered_elems
