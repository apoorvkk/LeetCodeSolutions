'''
URL: https://leetcode.com/problems/design-tic-tac-toe/
Time complexity: O(1)
Space complexity: O(n)
'''

class Player:
    def __init__(self, n):
        self.rows = [n for i in range(n)]
        self.columns = [n for i in range(n)]
        self.top_left_dig = n
        self.top_right_dig = n

class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.players = []
        self.players.append(Player(n))
        self.players.append(Player(n))
        self.n = n

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        curr_player = self.players[player-1]

        curr_player.rows[row] -= 1
        curr_player.columns[col] -= 1

        if row == col:
            curr_player.top_left_dig -= 1

        if row == (self.n - 1 - col):
            curr_player.top_right_dig -= 1

        if 0 in (curr_player.rows[row], curr_player.columns[col], curr_player.top_left_dig, curr_player.top_right_dig):
            return player
        return 0



# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
