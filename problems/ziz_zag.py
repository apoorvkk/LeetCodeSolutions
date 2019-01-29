class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        P      A     H     N 
          A   P  L  S  I  I  G
            Y      I     R
            
        3 rows -> every 4 letters
        4 rows -> every 6 letters
        5 rows -> every 8 letters
        6 rows -> 10 letters
        7 rows -> 12
        
        every 8 letters -> every 0 letters -> every 8 letters ->...
        every 6 letters -> every 2 letters -> every 6 letters -> ...
        
        
        X         X
          \      / \
            \   /    \
             \ /      \
              -         _  
        """
        if numRows == 1:
            return s
        if numRows > len(s):
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