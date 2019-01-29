class Solution:
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        
        [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]
        
        [
            [-80,-13,22],
            [83, 94,-5],
            [73,-48,61]]
        """
        memo = [[None for i in range(len(A[0]))] for j in range(len(A))]
        
        curr_min_sum = float('inf')
        
        
        for i in range(len(A)):
            min_sum = self._min_falling(memo, (0, i), A)
            curr_min_sum = min(min_sum, curr_min_sum)
            
        return curr_min_sum
    
    def _min_falling(self, memo, curr_pos, A):
        x, y = curr_pos
        
        next_row = x+1
        
        if next_row >= len(A):
            return A[x][y]
        
        curr_min_sum = float('inf')
        curr_column_selected = None
        
        next_columns = [y-1, y, y+1]
        for next_column in next_columns:
            if next_column < 0 or next_column >= len(A[0]):
                continue
                
            if memo[next_row][next_column] is not None:
                child_min_sum = memo[next_row][next_column]
            else:
                child_min_sum = self._min_falling(memo, (next_row, next_column), A)
            
            if A[x][y] + child_min_sum < curr_min_sum:
                curr_min_sum = child_min_sum + A[x][y]
                curr_column_selected = next_column
        
        memo[x][y] = curr_min_sum
        return curr_min_sum
        
        
        