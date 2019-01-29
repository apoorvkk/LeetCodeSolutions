from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
    
        A = [1,0,1,0,1], S = 2
        
        {
            # cumul_sum: num unique indices
            0: {-1}
            1: {0, 1}
            2: {2, 3}
            3: {4}
        }
        
        count = 4
        [0,0, 0, 1, 0, 0]
        
        {
        0: 3
        1: 1
        }
        count = 6
        
        
        [0,0,0]
        count = 6
        
        {
            0: 4,
            
        }
        """
        
        count = 0
        prefix_sums = defaultdict(int)
        

        prefix_sums[0] = 1
        
        cumul_sum = 0
        for index, val in enumerate(A):
            cumul_sum += val
            count += prefix_sums[cumul_sum-S]
            
            prefix_sums[cumul_sum] += 1
            
                
        
        
        return count
        
        