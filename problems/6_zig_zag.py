'''
URL: https://leetcode.com/problems/zigzag-conversion
Time complexity: O(n)
Space complexity: O(1)
'''

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows > len(s):
            return s

        zigzag = ""
        total_every_n = numRows * 2 - 2
        for i in range(numRows):
            every_n = (numRows-i) * 2 - 2
            move_n = [every_n, total_every_n - every_n]

            if move_n[0] == 0:
                move_n[0] = move_n[1]
            elif move_n[1] == 0:
                move_n[1] = move_n[0]

            curr_pos = i
            curr_move = 0
            while curr_pos < len(s):
                zigzag += s[curr_pos]
                curr_pos += move_n[curr_move]

                curr_move = int(not curr_move)
        return zigzag
