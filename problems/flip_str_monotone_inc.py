class Solution:
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        
        010101 | 101101
        
        001X
        012
        
        000000
        """
        
        total_zeros = sum(1 for i in range(len(S)-1, -1, -1) if S[i] == '0')
        total_ones = sum(1 for i in range(len(S)-1, -1, -1) if S[i] == '1')
        min_flips = total_zeros
        
        num_zeros = total_zeros  # num zeros in right subarray
        num_ones = 0 # num ones in left subarray
        
        divider = 0
        while divider < len(S):
            if S[divider] == '0':
                num_zeros -= 1
            else:
                num_ones += 1
            
            min_flips = min(min_flips, num_zeros + num_ones)
            divider += 1
            
        return min(min_flips, total_ones)
        