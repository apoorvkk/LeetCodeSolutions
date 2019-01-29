class Solution(object):
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        
        X .... A    2A
        i      2i  2i+1
        
        i     2i  2i+1
        0 .   0 .  1
        1 .   2 .  3
        2 .   4    5
        3     6 .  7
        4 .   8 .  9
        5     10   11
        6     12 . 134 
        
        [2, 4, 8, 16, _, _, _, _, _, _, _, _, _, _, _]
        
        
        [4,-2,2,-4, 8, 16]
        
        {
            4: (2, 8),
            -2: (-1, -4),
            2: (1, 4),
            -4: (-2, -8),
            8: (4, 16),
            16: (8, 32)
        }
        
        
        {
            4: (2, 8),
            -2: (-1, -4),
            2: (1, 4),
            -4: (-2, -8)
        }
        
        16, 8
        4, 2
        -2, -4
        """
        A.sort(reverse=True)
        vals = {}
        
        for num in A:
            if num in vals:
                vals[num] += 1
            else:
                vals[num] = 1 
        
        for num in A:
            if num not in vals:
                continue
                
            if num % 2 == 0 and (num // 2) in vals:
                vals[num] -= 1
                vals[num // 2] -= 1
                
                if vals[num] == 0:
                    del vals[num]
                if (num // 2) in vals and vals[num // 2] == 0:
                    del vals[num // 2]
                    
            elif (num * 2) in vals:
                vals[num] -= 1
                vals[num * 2] -= 1
                
                if vals[num] == 0:
                    del vals[num]
                if (num * 2) in vals and vals[num * 2] == 0:
                    del vals[num * 2]

        
        return len(vals) == 0
        
        