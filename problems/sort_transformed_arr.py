class Solution:
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        
        
        ----- ++++++
        
        a < 0
            b < 0
                x > 0
                    no change
                x < 0
                    no change
            b = 0 ax^2 + c
                reverse list
            b > 0
                x > 0
                    
                x < 0
        a = 0
            b < 0 ***
                reverse list
            b = 0
                no change
            b > 0
                no change
        a > 0
            b < 0
                flip negs
                
            b = 0 ax^2 + c
                flip negatives
                
            b > 0
                flip negatives
        a = -2
        b = 44
        c = -56
        
        0 = -2x^2 + 44x -234
        
       
        """
        f = lambda x: a*(x**2) + b*x + c
        
       
        
        start, end = 0, len(nums)-1
        f_vals = [None] * len(nums)
        curr_index = 0 if a < 0 else len(nums)-1 
        
        while start <= end:
            start_f = f(nums[start])
            end_f = f(nums[end])
            
            
            if a < 0: # inverted parabola
                if start_f < end_f:
                    f_vals[curr_index] = start_f
                    start += 1
                else:
                    f_vals[curr_index] = end_f
                    end -= 1
                curr_index += 1
            else: # upright parabola a> 0
                if start_f > end_f:
                    f_vals[curr_index] = start_f
                    start += 1
                else:
                    f_vals[curr_index] = end_f
                    end -= 1
                curr_index -= 1
        
        return f_vals
    