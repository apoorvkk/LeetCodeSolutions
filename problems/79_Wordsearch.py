'''
URL: https://leetcode.com/problems/word-search/description/
Time complexity: O(n*m)
Space complexity: O(n*m)
'''

from collections import defaultdict

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool

        1. Find first letter positions
        2. Iterate over first letter positions and do dfs
        """
        if len(word) == 0: return False

        # Find first letter positions
        positions = []
        first_letter = word[0]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == first_letter:
                    positions.append((i, j))

        for curr_position in positions:
            visited = defaultdict(bool)
            path_found = self.aux_exist(curr_position, word, 1, visited, board)
            if path_found: return True
        return False

    def aux_exist(self, curr_position, word, index, visited, board):
        if index >= len(word):
            return True

        next_letter = word[index]
        visited[curr_position] = True

        potential_positions = []
        potential_positions.append((curr_position[0], curr_position[1] + 1)) # right
        potential_positions.append((curr_position[0], curr_position[1] - 1)) # left
        potential_positions.append((curr_position[0] + 1, curr_position[1])) # south
        potential_positions.append((curr_position[0] - 1, curr_position[1])) # north


        for position in potential_positions:

            if 0 <= position[0] < len(board) and 0 <= position[1] < len(board[0]): # Validate position

                if not visited[position] and next_letter == board[position[0]][position[1]]:
                    path_found = self.aux_exist(position, word, index+1, visited, board)

                    if path_found:
                        return True

        visited[curr_position] = False
        return False

