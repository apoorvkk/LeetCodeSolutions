'''
URL: https://leetcode.com/problems/n-queens
'''

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n == 0:
            return []

        solutions = []

        self._aux_find_queen_positions(solutions, [], n)

        return self._construct_solutions(solutions)

    def _construct_solutions(self, solutions):
        board_solutions = []

        for solution in solutions:
            board = []
            row_to_column = [None for i in range(len(solution))]
            for column, row in enumerate(solution):
                row_to_column[row] = column

            for queen_column_pos in row_to_column:
                row_print = "." * (queen_column_pos) + "Q" + "." * (len(solution) - queen_column_pos - 1)
                board.append(row_print)
            board_solutions.append(board)
        return board_solutions

    def _find_available_positions(self, curr_solution, n):
        available_positions = set([i for i in range(n)])

        new_column_index = len(curr_solution)
        for column, row in enumerate(curr_solution):
            if row in available_positions:
                available_positions.remove(row)

            upper_diag = row + (new_column_index-column)
            lower_diag = row - (new_column_index-column)
            if upper_diag in available_positions:
                available_positions.remove(upper_diag)
            if lower_diag in available_positions:
                available_positions.remove(lower_diag)

        return available_positions

    def _aux_find_queen_positions(self, solutions, curr_solution, n):
        if len(curr_solution) == n:
            solutions.append(curr_solution)
            return

        available_positions = self._find_available_positions(curr_solution, n)
        for pos in available_positions:
            self._aux_find_queen_positions(solutions, curr_solution+[pos], n)


